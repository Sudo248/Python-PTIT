isPrime = [1]*1001
isPrime[0] = isPrime[1] = 0
for i in range(2, 1001):
    if isPrime[i]:
        for j in range(i*i, 1001, i):
            isPrime[j] = 0

a = input().split()
n,m = int(a[0]), int (a[1])

a = [[]]*n
for i in range(n):
    a[i] = [int(j) for j in input().split()]

for i in range(n):
    for j in range(m):
        print(isPrime[a[i][j]], end=" ")
    print()

