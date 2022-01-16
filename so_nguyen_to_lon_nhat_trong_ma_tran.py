# MAX = 1000
# isPrime = [False]*1001
import math
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

n, m = map(int, input().split())
a = [[]]*n
for i in range(n):
    a[i] = [int(i) for i in input().split()]

MAX = 0
for i in a:
    for j in i:
        if isPrime(j) and MAX < j:
            MAX = j
if MAX == 0:
    print("NOT FOUND")
else:
    print(MAX)
    for i in range(n):
        for j in range(m):
            if a[i][j] == MAX:
                print(f"Vi tri [{i}][{j}]")

