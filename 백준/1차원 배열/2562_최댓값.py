x = [int(input()) for _ in range(9)] # [ ]: 리스트로 만든다, _: 변수를 사용하지 않는다.
y = max(x)                    
z= x.index(y) + 1 # .index: 리스트 안의 해당값의 위치를 찾음
print(y)
print(z)