import random 
number = random.randint(1,100)
count = 0

print("Up & Down 술게임을 시작하겠습니다!")
while True:
    x = int(input("숫자를 입력해 주세요. : "))
    count += 1 
    if x < 1 or 100 < x :
        print("다시 입력해주세요.")
    elif number < x :
        print("Down")
    elif number > x:
        print("Up")
    elif number == x:
        print(f"{count}번 만에 정답을 맞추셨습니다.")
        break


#f-string : (f"문자열 {변수} 문자열")