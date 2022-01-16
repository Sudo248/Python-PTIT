s = input()
res = ""
dem = 0
for i in range(len(s)-1, -1, -1):
    res = s[i] + res
    dem += 1
    if dem == 3 and i > 0:
        res = ',' + res
        dem = 0

print(res)