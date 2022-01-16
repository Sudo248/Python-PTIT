import math
def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

t = int(input())
while t:
    t -= 1
    n = 0
    for i in input():
        n += int(i)
    print("YES" if isPrime(n) else "NO")