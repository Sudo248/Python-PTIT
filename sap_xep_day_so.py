t = int(input())
while t > 0 :
    t -= 1
    n,k = map(int,input().split())
    a = [int(i) for i in input().split()]
    m = max(a)
    index = a.index(m)
    a.insert(index, k)
    l,r = [],[]
    for i in a:
        if i < 0: l.append(i)
        else: r.append(i)
    print(*l, *r)