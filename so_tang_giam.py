t = int(input())

while t > 0:
    t -= 1
    s = input()
    ok = False
    for i in range(len(s)-1):
        if s[i] < s[i+1] and not ok:
            continue
        elif s[i] > s[i+1]:
            ok = True
            continue
        else:
            ok = False
            break
    print("YES" if ok else "NO")