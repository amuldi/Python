import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# CSV 불러오기
df = pd.read_csv(r"C:\Users\dldud\Downloads\산림청 국립산림과학원_대형산불위험예보목록정보_20250228.csv", encoding='cp949')
  # ← 본인 경로로 수정!

# 파생 변수 생성
df['예보일시'] = pd.to_datetime(df['예보일시'], errors='coerce')
df['월'] = df['예보일시'].dt.month
df['시간'] = df['예보일시'].dt.hour

# 위험도 타깃 정의: 실효습도 < 30 and 풍속 > 15 → 위험(1), 아니면 안전(0)
def define_risk(row):
    return 1 if row['실효습도'] < 30 and row['풍속'] > 15 else 0

df['위험도_이진'] = df.apply(define_risk, axis=1)

# 입력 변수
X = df[['시도명', '월', '시간', '실효습도', '풍속']]
y = df['위험도_이진']

# 전처리: 시도명 → 원핫인코딩
categorical_features = ['시도명']
numerical_features = ['월', '시간', '실효습도', '풍속']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_features),
        ('num', 'passthrough', numerical_features)
    ]
)


# 파이프라인 구성
from sklearn.linear_model import LogisticRegression

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=200, class_weight='balanced'))
])


# 훈련/검증 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model.fit(X_train, y_train)


# 예측
y_pred = model.predict(X_test)

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 윈도우 한글 폰트 경로 지정 (예: 맑은 고딕)
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
# 혼동 행렬 시각화
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['안전', '위험'], yticklabels=['안전', '위험'])
plt.xlabel("예측값")
plt.ylabel("실제값")
plt.title("혼동 행렬 (Confusion Matrix)")
plt.tight_layout()
plt.show()

# 변수 중요도 시각화
ohe = model.named_steps['preprocessor'].transformers_[0][1]
ohe_features = ohe.get_feature_names_out(['시도명'])
all_features = list(ohe_features) + numerical_features
coefs = model.named_steps['classifier'].coef_[0]

importance_df = pd.DataFrame({
    '변수': all_features,
    '계수(영향력)': coefs
}).sort_values(by='계수(영향력)', key=abs, ascending=False)


y_pred = model.predict(X_test)
plt.figure(figsize=(8, 5))
sns.barplot(data=importance_df, x='계수(영향력)', y='변수', palette='Blues_r')
plt.title("로지스틱 회귀 변수 중요도")
plt.tight_layout()
plt.show()
# 성능 보고서 출력
print(classification_report(y_test, y_pred))
