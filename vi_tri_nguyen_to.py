import math
def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

t = int(input())
csnt = ['2', '3', '5', '7']
while t:
    t -= 1
    ok = True
    for index, value in enumerate(input()):
        if value in csnt:
            if(not isPrime(index)):
                ok = False
                break
        else:
            if(isPrime(index)):
                ok = False
                break
    print("YES" if ok else "NO")

       