from itertools import combinations
n,k = map(int,input().split())
a = list(set([int(i) for i in input().split()]))
a.sort()
res = combinations(a,k)
for i in res:
    for j in i:
        print(j,end=' ')
    print()

