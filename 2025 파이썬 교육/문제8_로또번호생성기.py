import random
number = int(input("첫 번째 번호를 뽑으세요. : "))
if 1 <= number <= 45:
    Lotto = [number]
    x = list(range(1,46))
    x.remove(number)
    Lotto += random.sample(x, 5) 
    print("생성된 로또 번호는",Lotto,"입니다.")
else:
    print("다시 입력해주세요.")
