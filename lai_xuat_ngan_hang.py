t = int(input())
while t:
    t -= 1
    n, x, m = map(float, input().split())
    dem = 0
    x /= 100
    while n < m:
        dem += 1
        n += n*x
    print(dem)