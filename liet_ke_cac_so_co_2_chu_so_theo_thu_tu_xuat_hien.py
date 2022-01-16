s = input()
res = []
for i in range(1,len(s),2):
    tmp = int(f'{s[i-1]}{s[i]}')
    if tmp not in res:
        res.append(tmp)
print(*res)