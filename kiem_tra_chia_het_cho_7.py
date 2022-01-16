t = int(input())
while t > 0:
    t -= 1
    n = input()
    res = int(n)
    for i in range(1001):
        if res % 7 == 0:
            break
        res = int(n) + int(n[::-1])
        n = str(res)
    print(res if res % 7 == 0 else -1)