s = input()
res = {}
for i in range(1,len(s),2):
    tmp = int(f'{s[i-1]}{s[i]}')
    res[tmp] = res[tmp] +1 if tmp in res else 1

for key, val in res.items():
    print(key, val)