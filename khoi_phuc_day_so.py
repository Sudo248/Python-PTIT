n = int(input())
a = [[]]*n
for i in range(n):
    a[i] = [int(j) for j in input().split()]

if n == 2:
    res = a[0][1] // 2
    print(res, res)
else:
    a1 = (a[1][2] - a[0][2] + a[0][1]) // 2
    a0 = a[0][1] - a1
    print(a0, a1, end=' ')
    for i in range(2,n):
        print(a[0][i] - a0,end=' ')