n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):

    x,y = map(int,input().split())
    for _x in range(x,x + 10):
        for _y in range(y,y + 10):
            if _x >= 100 or _y >= 100:
                break
            paper[_x][_y] = 1
sum = 0
for row in range(100):
    sum += paper[row].count(1)

print(sum)