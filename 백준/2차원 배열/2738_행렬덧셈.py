N, M = map(int, input().split())

# 첫 번째 행렬 입력
A = [list(map(int, input().split())) for _ in range(N)]

# 두 번째 행렬 입력
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ")
    print()