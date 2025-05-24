N,X=map(int,input().split())
y = list(map(int,input().split()))
for i in range(N):
    if y[i]<X:
        print(y[i],end=" ") # end = " ": 줄바꿈 대신 공백 사용 