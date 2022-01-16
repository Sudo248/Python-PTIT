def cmp(x):
    res = 0
    for i in x:
        res += int(i)
    return res,int(x)

t = int(input())
while t:
    t -= 1
    n = int(input())
    a = [i for i in input().split()]
    for i in sorted(a,key=cmp):
        print(i,end=' ')
    print()