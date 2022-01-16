s = input()
k = int(input())
res = {}
for i in range(1,len(s),2):
    tmp = int(f'{s[i-1]}{s[i]}')
    res[tmp] = res[tmp] +1 if tmp in res else 1

res = sorted(res.items())
ok = True
for key, val in res:
    if val >= k:
        print(key, val)
        ok = False

if ok: print("NOT FOUND")