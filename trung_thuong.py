t = int(input())
while t:
    t -= 1
    n = int(input())
    a = {}
    for i in range(n):
        x = int(input())
        if x in a: a[x] += 1
        else: a[x] = 1
    max_val = max(a.values())
    arr = sorted(a.keys())
    for i in arr:
        if a[i] == max_val:
            print(i)
            break