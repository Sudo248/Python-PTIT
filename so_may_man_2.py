t = int(input())
while t:
    t -= 1
    check = True
    for i in input():
        if i != '4' and i != '7': 
            check = False
            break
    print("YES" if check else "NO")
