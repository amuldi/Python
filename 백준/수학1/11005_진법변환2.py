N, B = input().split()
N = int(N)
B = int(B)

if N == 0:
    print(0)
else:
    result = ''
    while N > 0:
        remainder = N % B
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        N = N // B
    print(result)
