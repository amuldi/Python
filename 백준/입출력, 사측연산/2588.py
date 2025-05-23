a = int(input())
b = int(input())
b1= b%10 #1의 자리 분리
b2= (b//10)%10 # 10의 자리 분리
b3= (b//100)%10 #100의 자리 분리
print(a*b1)
print(a*b2)
print(a*b3)
print(a*b) 