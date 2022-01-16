t = int(input())
while t:
    t -= 1
    a = [int(i) for i in input()]
    i = len(a)-2
    while i >= 0 and a[i] <= a[i+1]: i-=1
    if i < 0:
        print(-1)
        continue
    j = len(a) -1
    Max, ind = 0,i
    while j>i:
        if a[j] < a[i] and Max <= a[j]:
            Max = a[j]
            ind = j
        j -= 1
    if i == 0 and a[ind] == 0:
        print(-1)
        continue
    a[i], a[ind] = a[ind], a[i]
    for i in a: print(i,end='')
    print()