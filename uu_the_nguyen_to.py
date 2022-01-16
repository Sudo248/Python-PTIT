import math
def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

t = int(input())
while t:
    t -= 1
    n = input()
    if not isPrime(len(n)):
        print("NO")
    else:
        dem=0
        for i in n:
            if isPrime(int(i)): dem+=1
        print("YES" if dem > len(n)/2 else "NO")
