import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# 데이터 불러오기 (경로는 본인 환경에 맞게 수정)
file_path = r"C:\Users\dldud\Downloads\산림청 국립산림과학원_대형산불위험예보목록정보_20250228.csv"
data = pd.read_csv(file_path, encoding="cp949")

#  위험도 분류 함수 정의 (연관 분석 대상 라벨용 아님, 조건 필터에 사용)
def classify_risk(row):
    if row['실효습도'] < 30 and row['풍속'] > 7:
        return '높음'
    elif 30 <= row['실효습도'] < 40 and 5 < row['풍속'] <= 7:
        return '보통'
    else:
        return '낮음'

#  위험도 컬럼 생성
data['위험도'] = data.apply(classify_risk, axis=1)

# 연관분석용 데이터 추출 (위험도가 '높음'인 경우만 필터링)
high_risk_df = data[data['위험도'] == '높음'][['실효습도', '풍속']].copy()

#  수치형 컬럼을 범주형으로 변환 (구간화, qcut 사용)
for col in high_risk_df.columns:
    high_risk_df[col] = pd.qcut(high_risk_df[col], q=3, duplicates='drop').astype(str)

# 각 행을 거래(transaction) 형식으로 리스트로 변환
transactions = high_risk_df.values.tolist()

#  TransactionEncoder로 one-hot 인코딩 수행
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_trans = pd.DataFrame(te_ary, columns=te.columns_)

# apriori 알고리즘 적용 (최소 지지도 1%)
frequent_itemsets = apriori(df_trans, min_support=0.01, use_colnames=True)

#  연관 규칙 생성 (신뢰도 0.3 이상)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)

# lift 기준 내림차순 정렬된 상위 10개 규칙 출력
print(rules.sort_values(by='lift', ascending=False).head(10))
