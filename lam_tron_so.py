t = int(input())
while t:
    t -= 1
    a = [int(i) for i in input()]
    nho = 0
    res = ""
    for i in range(len(a)-1,-1,-1):
        if i == 0:
            a[i] += nho
            res = str(a[i]) + res
            break
        if a[i] + nho >= 5:
            nho = 1
        else: nho = 0
        res = '0' + res
    print(res)
            
    