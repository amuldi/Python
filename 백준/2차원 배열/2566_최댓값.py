maxnum = -1 # 최댓값을 저장할 변수
row, col = 0,0 # 최댓값 위치

for i in range(9):
    number = list(map(int,input().split()))
    for j in range(9): # 각 행의 숫자 확인
        if number[j] > maxnum: # 더 큰 값이 나올시 갱신
            maxnum = number[j]
            row, col = i+1,j+1 # 1부터 시작하므로 +1 로 위치 저장

print(maxnum)
print(row,col)