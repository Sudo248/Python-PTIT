import math
def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0: return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
b = []
Sum = 0
for i in a:
    if i not in b:
        b.append(i)
        Sum += i
lSum = 0
for i in range(len(b)):
    lSum += b[i]
    if isPrime(lSum) and isPrime(Sum-lSum):
        print(i)
        break
if lSum == Sum: print("NOT FOUND")