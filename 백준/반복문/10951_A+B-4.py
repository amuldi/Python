while True:
 try: #오류가 나면 except로 넘어감
    A,B=map(int,input().split())
    print(A+B)
 except : #오류감지 후 breakㄹ 넘어감
    break

   