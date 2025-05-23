A,B = map(int,input().split())
if -10000<= A <=10000 and -10000<= B <=10000:
  if A>B: print(">") 
  elif A<B: print("<")
  else : print("==")