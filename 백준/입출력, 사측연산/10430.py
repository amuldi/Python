A,B,C = map(int,input().split()) # map : 입력시 옆으로 정렬, .split : 입력시 한칸씩 띄움
if 2<= A <=10000 and 2<= B <=10000 and 2<=C<=10000:
    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)