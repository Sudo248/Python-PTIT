t = int(input())
while t:
    t -= 1
    n = 0
    for i in input():
        n += int(i)
    if n > 9 and n == int(str(n)[::-1]): print("YES")
    else: print("NO")