import math
def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True
def ok(s):
    n = 0
    #vt chan
    for i in s[::2]:
        x = int(i)
        if x % 2 != 0: return False
        n += x

    #vt le
    for i in s[1::2]:
        x = int(i)
        if x % 2 ==0: return False
        n += x
    return isPrime(n)
    
t = int(input())
while t:
    t -= 1
    print("YES" if ok(input()) else "NO")
