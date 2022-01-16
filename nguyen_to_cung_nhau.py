import math
n,k = map(int, input().split())
begin, end = 10**(k-1), 10**k
dem = 0
for i in range(begin,end):
    if math.gcd(n,i) == 1:
        print(i,end=' ')
        dem += 1
        if dem == 10: 
            dem = 0
            print()
    