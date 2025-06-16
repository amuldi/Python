x = [i for i in range(1,31)] 
for _ in range(28):
 y = int(input())
 x.remove(y) #x 리스트에서 그 숫자를 제거
print(min(x))
print(max(x))

#x = [i for i in range(1, 31)]  # 전체 학생
#for _ in range(28):            # 과제 낸 학생 수
#    y = int(input())           # 과제 낸 학생 번호 입력받기
#    x.remove(y)                # 그 학생을 전체 리스트에서 제거
#print(min(x))                  # 번호가 더 작은 학생#
#print(max(x))                  # 번호가 더 큰 학생