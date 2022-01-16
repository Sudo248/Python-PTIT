
t = int(input())
while t > 0 :
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    a.sort()
    b.sort()

    ok = True

    for i in range(n):
        if a[i] > b[i]:
            ok = False
            break
    print("YES" if ok else "NO")

