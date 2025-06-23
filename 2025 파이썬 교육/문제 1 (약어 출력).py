x,y,z = map(str,input("단어를 입력하세요 : ").split())
list = [x,y,z]
a = list[0][0]
b = list[1][0]
c = list[2][0]
if a == b == c :
    print("다시 입력해주세요.")
else :
    print(a,b,c)