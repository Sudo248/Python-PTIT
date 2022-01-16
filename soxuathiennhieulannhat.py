
from typing import Counter


t = int(input())
while t>0:
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    b = Counter(a)
    n = n / 2
    ok = True
    for i in b:
        if b[i] > n:
            print(i)
            ok = False
            break
    if ok == True:
        print("NO")  

    
    
        


