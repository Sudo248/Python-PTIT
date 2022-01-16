import math
def gcd(a, b):
    while a*b > 0:
        if a > b: a %= b
        else: b %= a
    return a+b

t = int(input())
while t:
    t -= 1
    n = int(input())
    k = 0
    for i in range(1,n+1):
        if gcd(i,n) == 1:
            k += 1
    if k < 2:
        print("NO")
    else:
        ok = True
        for i in range(2,int(math.sqrt(k)+1)):
            if k % i == 0:
                ok = False
                break
        print("YES" if ok else "NO")

