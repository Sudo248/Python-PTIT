import math
t = int(input())
while t:
    t -= 1
    n = input()
    m = int(n[::-1])
    n = int(n)
    print("YES" if math.gcd(n,m) == 1 else "NO")