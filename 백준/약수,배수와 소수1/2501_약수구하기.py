n, k = map(int, input().split())
x = []
for i in range(1, n + 1):
    if n % i == 0:
        x.append(i)
print(x[k - 1]if len(x) >= k else 0)