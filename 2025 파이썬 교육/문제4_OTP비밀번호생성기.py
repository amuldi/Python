import random 
alphabet = "abcdefghijklmnopqrsguvwsyz01234567889"
Maker_password= ""

for _ in range (3):
    Maker_password =""
    for _ in range (6):
         Maker_password += random.choice(alphabet)

    print("OTP비밀번호:",Maker_password)
