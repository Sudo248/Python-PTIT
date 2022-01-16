s = input()
res = set()
for i in range(1,len(s),2):
    res.add(int(f'{s[i-1]}{s[i]}'))
print(*sorted(res))