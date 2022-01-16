t = int(input())
while t>0:
    t -= 1
    m = ['0','1','2']
    ok = True
    for i in set(input()):
        if i not in m:
            ok = False
            break
    print("YES" if ok else "NO")
