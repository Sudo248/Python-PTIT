import re
from typing import Counter
def cmp(x):
    return -x[1], x[0]

n = int(input())
res = []
for i in range(n):
    res.extend(re.findall('[a-zA-z]+',input().lower()))
res = Counter(res)
res = sorted(res.items(), key=cmp)
for key, val in res:
    if key != '':
        print(key, val)