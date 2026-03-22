x = int(input())

y = 2
while y * y <= x:
    while x % y == 0:
        print(y)
        x //= y
    y += 1

if x > 1:
    print(x)
