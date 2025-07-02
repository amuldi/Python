N,M = map(int,input().split())
basket = [0]*N # 바구니를 0으로 초기화
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i - 1, j):  # 바구니 번호는 1부터 시작하므로 -1
        basket[x] = k #x번째 값을 k로 바꿈
print(*basket) #리스트를 깔끔하게 공백으로 나눠 출력