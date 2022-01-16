a,k,n = map(int, input().split())

if a < k:
    b = k - a
else:
    b = a % k

a += b
if a > n:
    print(-1)
else:
    while a <= n:
        print(b,end=' ')
        b += k
        a += k
