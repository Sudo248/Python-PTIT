t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    ok = True
    for i in range(n):
        if a[i] > b[i]:
            ok = False
            break
    print("YES" if ok else "NO")