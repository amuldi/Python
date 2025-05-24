T = int(input())
for i in range(1,T+1):
  A,B= map(int,input().split())
  print(f"Case #{i}: {A+B}") # f-string : 문자열 안에 {}를 넣어 변수를 표현