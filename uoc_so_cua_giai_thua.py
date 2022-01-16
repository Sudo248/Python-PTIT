t=int(input())
while t:
    t -= 1
    n, p = map(int, input().split())
    res = 0
    for i in range(p,n+1,p):
        while i % p == 0:
            res += 1
            i /= p
    print(res)