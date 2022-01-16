import math
def gcd(a ,b):
    while a*b > 0:
        if a > b: a %= b
        else: b %= a
    return str(a+b)

def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,int(math.sqrt(n)),6):
        if n %i == 0 or n % (i+2) == 0:
            return False
    return True

def my_sum(n):
    res = 0
    for i in str(n):
        res += int(i)
    return res

t = int(input())
while t:
    t -= 1
    a,b = map(int, input().split())
    print("YES" if isPrime(my_sum(gcd(a,b))) else "NO")