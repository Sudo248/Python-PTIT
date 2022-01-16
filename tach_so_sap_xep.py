n = int(input())
a = []
while n:
    n -= 1
    s = input()
    res = ""
    i = 0
    while i < len(s):
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            res = res + s[i]
            i += 1
        if res != "":
            a.append(int(res))
            res = ""
            continue
        i += 1
a.sort()
for i in a:
    print(i)
