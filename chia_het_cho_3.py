t = int(input())
while t:
    t -= 1
    n = 0
    for i in input():
        n += int(i)
    print("YES" if n%3==0 else "NO")