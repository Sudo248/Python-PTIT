t = int(input())
while t:
    t -= 1
    s = input()
    tich = 1
    ok = False
    for i in s[::2]:
        if i != '0':
            tich *= int(i)
            ok = True
    print(tich if ok else 0, sum([int(i) for i in s[1::2]]) )