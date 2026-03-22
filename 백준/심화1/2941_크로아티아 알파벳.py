alphabet = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in croatia:
    alphabet = alphabet.replace(i, "*") # replace = 문자열 치환 / 사용법 : 문자열.replace(찾을문자열, 바꿀문자열) , 
print(len(alphabet))