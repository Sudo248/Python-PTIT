n, m = map(int, input().split())
a = [[]]*(n+1)
for i in range(n):
    a[i] = input().split()
if n > m:
    dem = 0
    for i in range(n):
        if dem < n-m and i % 2 == 0:
            dem += 1
        else:
            for j in range(m):
                print(a[i][j], end=' ')
            print()
else:
    for i in range(n):
        dem = 0
        for j in range(m):
            if dem < m - n and j % 2 == 1:
                dem += 1
            else:
                print(a[i][j], end=' ')
        print()
