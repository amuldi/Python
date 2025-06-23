total = 0
i = 0
x = int(input("한달 납입 금액은? : "))
if x < 500:
    print("액수가 적습니다 돌아가세요.")
else:
    a, b = map(int, input("금리(%)와 목표금액은? : ").split())
    while total < b:
        total += x
        total += total * (a / 100 / 12)
        i += 1
    print(i+"개월")