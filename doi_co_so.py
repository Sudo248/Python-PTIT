mau = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

t = int(input())
while t:
    t -= 1
    n,m = map(int,input().split())
    res = ""
    while n:
        res = mau[n%m] + res
        n //= m
    print(res)

