MAX = 10**4 + 5
dd = [True for i in range(MAX)]
dd[0] = dd[1] = False
primes = []
for i in range(MAX):
    if dd[i]:
        primes.append(i)
        for j in range(i*i, MAX, i):
            dd[j] = False

n = input()
a = set([int(i) for i in input().split()])
res = 0
for i in a:
    if i not in primes:
        for j in range(len(primes)):
            if primes[j] > i:
                res = max(res,min(i - primes[j-1], primes[j] - i))
                break
print(res)