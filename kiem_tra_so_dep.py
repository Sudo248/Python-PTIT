t = int(input())
while t>0:
    t-=1
    s = input()
    ok = True
    if len(set(s)) !=  2:
        ok = False
    else:
        c = s[0]
        for i in range(0,len(s)-1):
            if s[i] == s[i+1]:
                ok = False
                break
    print("YES" if ok else "NO")