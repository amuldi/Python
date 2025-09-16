from datetime import datetime
name = input("이름 : ")
id = input("주민등록번호 : ")
ad = input("주소지 : ")

print("<<< 환자차트 >>>")

#이름
print("이름 : ",name[0] + "*" + name[2:])

#성별
if id[7] == "1" or id[7] == "3":   
    print("성별 : 남성")
elif id[7] == "2" or id[7] == "4": 
    print("성별 : 여성")
else :
    print("다시 입력해주세요.")

#나이
today = datetime.today()
gender = id[7]
century = 1900 if gender in ["1", "2"] else 2000
year = century + int(id[:2])
month = int(id[2:4])
day = int(id[4:6])
age = today.year - year
if (today.month, today.day) < (month,day):
    age -= 1
print("(만)나이 :", age,"세")

#주민등록번호
print("주민등록번호 : ",id[:6] + "-"+id[7]+"*****")

#주소지
if "구" in ad:
    cut = ad.index("구")
    print("주소지 : ", ad[:cut+1])
elif "군" in ad:
    cut = ad.index("군")
    print("주소지 : ",ad[:cut+1])
else:
    print("주소지 : ", ad)
