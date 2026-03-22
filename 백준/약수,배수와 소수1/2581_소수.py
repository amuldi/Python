m = int(input())
n = int(input())

primes = []

for num in range(m, n+1):
    if num < 2:
        continue

    prime = True
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
    
    if prime:
        primes.append(num)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))