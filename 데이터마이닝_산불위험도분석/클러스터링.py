import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# CSV 파일 로드 (한글 인코딩 cp949로 지정)
df = pd.read_csv(r"C:\Users\dldud\Downloads\산림청 국립산림과학원_대형산불위험예보목록정보_20250228.csv", encoding="cp949")

# 사용할 수치형 변수만 선택하고, 결측치 제거
X = df[['실효습도', '풍속']].dropna()

# 데이터 표준화 (평균 0, 표준편차 1로 변환하여 스케일 차이 제거)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#  Elbow Method를 통해 최적 클러스터 개수 탐색
inertia = []  # 클러스터 내부 거리 합을 저장할 리스트
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertia.append(km.inertia_)  # 각 k에 대한 inertia 저장

#  한글 폰트 설정 (맑은 고딕)
import matplotlib.font_manager as fm
font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows 환경 기준
fontprop = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=fontprop)
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 부호 깨짐 방지

#  Inertia 시각화: 클러스터 수(k)에 따른 비용 시각화 (Elbow Plot)
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('클러스터 수')
plt.ylabel('Inertia')  # 군집 내 거리 제곱합 (작을수록 좋음)
plt.title('Elbow Method')  # 팔꿈치처럼 꺾이는 지점이 최적 k
plt.show()

# 최적 k=3으로 설정하고 클러스터링 수행
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)  # 예측된 클러스터 결과를 원본 df에 저장

# 각 클러스터별 평균 실효습도와 풍속 값 확인
print(df.groupby('cluster')[['실효습도', '풍속']].mean())

