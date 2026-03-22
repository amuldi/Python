n = int(input())

# 대각선(층) 찾기
line = 0
count = 0
while count < n :
    line += 1
    count += line

# 찾은 대각선 안의 몇번째 분수인지 찾기
z = n - (count - line)  

if line % 2 == 0 :   # 짝수 대각선 
    numerator = z
    denominator = line - z + 1
    
else :               # 홀수 대각선
    numerator = line - z + 1
    denominator = z

print(f"{numerator}/{denominator}")

