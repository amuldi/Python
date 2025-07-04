N, M = map(int, input().split())
basket = [i + 1 for i in range(N)]  # 바구니에 번호와 같은 공이 들어 있음
for _ in range(M):
    i, j = map(int, input().split())
    basket[i - 1], basket[j - 1] = basket[j - 1], basket[i - 1]  # 공 바꾸기
print(*basket)