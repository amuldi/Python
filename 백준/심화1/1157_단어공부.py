alpha = input().strip().upper() # .upper() = 소문자를 대문자로 바꿈
count = [0] * 26 # 알파벳 개수 리스트

for i in alpha:
    x = ord(i) - ord('A') # 문자를 유니코드 정수값으로 바꾸고 'A'의 코드값을 뺌
    count[x] += 1 # 입력한 알파벳 개수세기

max_count = max(count) # 가장 많이 나온 알파벳 찾기

if count.count(max_count) > 1:
    print("?")
else:
    print(chr(count.index(max_count) + ord('A'))) # chr() = 코드값을 문자로 바꿈