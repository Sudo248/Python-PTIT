import math
begin, end = map(int, input().split())
for i in range(begin, end-1):
    for j in range(i+1, end):
        for k in range(j+1,end+1):
            if math.gcd(i,j) == 1 and math.gcd(i,k) == 1 and math.gcd(k,j) == 1:
                print(f'({i}, {j}, {k})')