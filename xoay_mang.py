t = int(input())
while t > 0:
    t -= 1
    n,k = map(int, input().split())
    a = [int(i) for i in input().split()]
    for i in range(k, n):
        print(a[i],end=' ')
    for i in range(k):
        print(a[i],end=' ')
    print()