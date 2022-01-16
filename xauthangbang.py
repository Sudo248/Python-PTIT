mau = "abcdefghijklmnopqrstuvwxyz"
dis = {}

for i in range(26):
    dis[mau[i]] = i

t = int(input())
while t:
    t -= 1
    s = input()
    i, j = 0, len(s)-1
    ok = True
    while i <= j:
        if abs(dis[s[i]] - dis[s[i+1]]) != abs(dis[s[j]] - dis[s[j-1]]):
            ok = False
            break
        i += 1
        j -= 1
    print("YES" if ok else "NO")
