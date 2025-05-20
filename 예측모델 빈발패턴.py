import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# ✅ 한글 폰트 설정 (macOS용)
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# ✅ 1. 파일 경로 입력 (실제 위치에 맞게 수정!)
file_path = "/Users/jsh/Desktop/데이터 마이닝/산림청 국립산림과학원_대형산불위험예보목록정보_20250228.csv"
data = pd.read_csv(file_path, encoding="cp949")

# ✅ 2. 위험도 구간화 함수 정의
def classify_risk(row):
    if row['실효습도'] < 30 and row['풍속'] > 7:
        return '높음'
    elif 30 <= row['실효습도'] < 40 and 5 < row['풍속'] <= 7:
        return '보통'
    else:
        return '낮음'

# ✅ 3. 위험도 컬럼 생성
data['위험도'] = data.apply(classify_risk, axis=1)
print("📌 위험도 분포:\n", data['위험도'].value_counts())

# ✅ 4. 데이터 분할 및 모델 학습
X = data[['실효습도', '풍속']]
y = data['위험도']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ 5. 예측 및 평가
y_pred = model.predict(X_test)
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))
print("\n🔀 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# ✅ 6. 혼동 행렬 시각화
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d',
            xticklabels=model.classes_, yticklabels=model.classes_, cmap='Blues')
plt.xlabel("예측 등급")
plt.ylabel("실제 등급")
plt.title("🔥 산불 위험도 예측 혼동 행렬")
plt.tight_layout()
plt.show()

# ✅ 7. 연관 규칙 분석: 예측이 '높음'인 조건만
df = X.copy()
df['predicted_risk'] = y_pred
high_risk_df = df[df['predicted_risk'] == '높음'].drop(columns=['predicted_risk'])

# 연속형 데이터를 범주형으로 구간화
for col in high_risk_df.columns:
    if high_risk_df[col].dtype != 'object':
        high_risk_df[col] = pd.qcut(high_risk_df[col], q=3, duplicates='drop').astype(str)

# 거래 형식으로 변환
transactions = high_risk_df.astype(str).values.tolist()
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_trans = pd.DataFrame(te_ary, columns=te.columns_)

# Apriori 및 연관 규칙 도출
frequent_itemsets = apriori(df_trans, min_support=0.1, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# ✅ 8. 규칙 결과 출력
print("\n📌 상위 연관 규칙 (lift 기준):")
print(rules.sort_values(by='lift', ascending=False).head(10))