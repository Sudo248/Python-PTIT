import math
from typing import Counter

def is_prime(n):
    if n < 2: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5,int(math.sqrt(n)),6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
dd = Counter(a)
for i in dd:
    if is_prime(i):
        print(i,dd[i])
