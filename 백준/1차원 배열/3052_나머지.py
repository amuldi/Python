x= set() #set(): 중복을 허용하지 않음
for _ in range (10):
    A = int(input()) 
    x.add(A%42) #나머지를 set에 추가
print(len(x)) # len(): 요소의 개수를 알려줌