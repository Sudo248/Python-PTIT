t = int(input())
while t:
    t -= 1
    res = ""
    s = 0
    for i in input():
        if i >= '0' and i <= '9':
            s += int(i)
        else: res += i
    print(''.join(sorted(res),s,sep=''))