lines = [input().rstrip() for _ in range(5)] # input()을 5번 반복하여 5번 입력받음
maxlen = max(len(line) for line in lines) # 가장 긴 줄을 maxlen에 저장
word = ""

for i in range(maxlen):
    for line in lines:
        if i < len(line):
            word += line[i] # 조건 만족 시 word에 이어붙이기
print(word)
