t = int(input())
while t:
    t -= 1
    n = int(input())
    so, mu = 3,0
    print(1, end='')

    while n%2==0:
        mu += 1
        n /= 2
    if mu >= 1:
        print(" * ",2,'^',mu,sep='',end='')
    mu = 0
    while n > 1:
        if n % so == 0:
            mu += 1
            n /= so
        else: 
            if mu > 0:
                print(" * ",so,'^',mu,sep='',end='')
            mu = 0
            so += 2

    if mu >= 1:
        print(" * ",so,'^',mu,sep='')
    else:
        print()