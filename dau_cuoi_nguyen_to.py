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
    if isPrime(int(n[:3])) and isPrime(int(n[-3:])):
        print("YES")
    else:
        print("NO")