#1330
#A,B = map(int,input().split())
#if -10000<= A <=10000 and -10000<= B <=10000:
#  if A>B: print(">") 
#  elif A<B: print("<")
#  else : print("==")

#9498
#score = int(input())
#if 90<=score<=100: 
#    print("A") 
#elif 80<=score<=89: 
#    print("B")
#elif 70<=score<=79: 
#    print("C")
#elif 60<=score<=69: 
#    print("D")
#else : 
#    print("F")

#2743
#x = int(input())
#if 1 <= x <= 4000:
#    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0): # x !=0 : x는 0이 아니다
#        print(1)
#    else:
#        print(0)

#14681
#x=int(input())
#y=int(input())
#if -1000<= x <=1000 and -1000<= y <= 1000 and x !=0 and y !=0: 
#  if (x>0 and y>0):
#    print(1)
#  elif(x<0 and y>0):
#    print(2)
#  elif(x<0 and y<0):
#    print(3)
#  elif(x>0 and y<0):
#    print(4)

#2884
#H,M = map(int,input().split())
#if 0<= H <= 23 and 0 <= M <= 59 :
#    if M>=45 :
#        M -= 45
#    else :
#     M += 15
#     H -= 1
#    if H <0:
#         H = 23
#print(H,M)

#2525
#A,B = map(int,input().split())
#C= int(input())
#A += C//60
#B += C%60
#if B >= 60 :
# A +=1
# B-=60
#if A >=24 :
# A-= 24
#print(A,B)

#2480
#A,B,C = map(int,input().split())
#if A==B==C :
# print(10000+A*1000) 
#elif A==B or A==C :
# print(1000+A*100)
#elif B==C:
# print(1000+B*100)
#else :
# print(max(A,B,C)*100)