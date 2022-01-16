import math
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

m = ['2','3','5','7']
def solve():
    s = input()
    if isPrime(len(s)):
        dem = 0
        for i in s:
            if i in m: dem += 1
        return "YES" if dem > (len(s)//2) else "NO"

    else:
        return "NO"
t = int(input())
while t > 0:
    t -= 1
    print(solve())


