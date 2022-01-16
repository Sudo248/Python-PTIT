t = int(input())
while t:
    t -= 1
    s = input()
    lens = len(s)
    if lens % 2 == 0 or s[0] == s[1]:
        print("NO")
    else:
        s1 = s[::2]
        ok = True
        for i in range(lens//2 - 1):
            if s1[i] != s1[i+1]:
                ok = False
                break
        print("YES" if ok else "NO")