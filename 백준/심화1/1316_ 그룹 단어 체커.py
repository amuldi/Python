x = int(input())

for i in range (x):
    word = input()
    for j in range(1,len(word)): # 입력한 단어를 2번째 글자부터 검사
        if word.find(word[j-1]) > word.find(word[j]): # .find = 인덱스 위치를 알려줌
            x -= 1
            break
print(x)

