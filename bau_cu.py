from typing import Counter
def cmp(x):
    return x[1], -x[0]
m, n = map(int,input().split())
a = Counter([int(i) for i in input().split()])
a = sorted(a.items(),key=cmp,reverse=True)
ok = True
for i in a:
    if i[1] != a[0][1]:
        print(i[0])
        ok = False
        break
if ok: print("NONE")