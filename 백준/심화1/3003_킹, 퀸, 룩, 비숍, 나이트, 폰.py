chess = [1,1,2,2,2,8]
x = list(map(int,input().split()))

for i in range(6):
    print(chess[i] - x[i], end = " ") # end = " " 줄바꿈대신 한칸 띄어서 출력 (" " 안의 공백만큼 띄움)
