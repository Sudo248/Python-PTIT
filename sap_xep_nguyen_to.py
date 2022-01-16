import math

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
for i in range(0, n-1):
    if snt(a[i]):
        for j in range(i+1, n):
            if a[i] > a[j] and snt(a[j]):
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp

print(*a)
