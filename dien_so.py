t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    b = set(range(min(a), max(a)+1))
    print(len(b.difference(set(a))))

     
    