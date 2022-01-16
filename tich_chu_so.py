t = int(input())
while t:
    t -= 1
    n = 1
    for i in input():
        if i != '0':
            n *= int(i) 
    print(n)