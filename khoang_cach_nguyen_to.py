n,x = map(int, input().split())
Prime = []
isPrime = [1]*10001
isPrime[0] = isPrime[1] = 0
for i in range(2,10001):
    if isPrime[i] == 1:
        Prime.append(i)
        n -= 1
        if n == 0:
            break
        for j in range(i*i,10001,i):
            isPrime[j] = 0

print(x,end=' ')
for i in Prime:
    x += i
    print(x,end=' ')