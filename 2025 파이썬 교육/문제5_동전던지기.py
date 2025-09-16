import random
coin = "AB"

while True: 
 x = input("계속하시겠습니까? :")
 if (x == "yes"):
    print(random.choice(coin))
 elif(x == "no"):
    print("안녕히가세요.")
    break
 else :
   print("다시입력하세요.")