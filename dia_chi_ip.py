t = int(input())
while t > 0:
    t -= 1
    a = input().strip().split('.')
    ok = True
    if len(a) != 4:
        ok = False
    else:
        for i in a:
            if i.isnumeric() and int(i) <= 255:
                continue
            else:
                ok = False
                break
    print("YES" if ok else "NO")