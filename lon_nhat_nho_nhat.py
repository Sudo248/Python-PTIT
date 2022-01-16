while True:
    n = int(input())
    if n == 0: break
    a = []
    while n:
        n -= 1
        a.append(int(input()))
    Max, Min = max(a), min(a)
    if Max == Min:
        print("BANG NHAU")
    else:
        print(Min, Max)