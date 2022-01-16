t = int(input())
while t > 0:
    t -= 1
    s = input()
    n = len(s)
    sum = int(s[n-1])
    check = True
    for i in range(n-1):
        if abs(int(s[i]) - int(s[i+1])) != 2: 
            check = False
            break
        sum += int(s[i])
    if sum % 10 != 0: check = False
    print("YES" if check else "NO")