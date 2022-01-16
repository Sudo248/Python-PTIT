import re
from typing import Counter
def cmp(x):
    return -x[1], x[0]

n, k = map(int, input().split())
res = []
for i in range(n):
    res.extend(re.findall('\w+',input().lower()))
res = Counter(res)
res = sorted(res.items(), key=cmp)
for key, val in res:
    if val >= k :
        print(key, val)