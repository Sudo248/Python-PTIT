n = int(input())
h, c = [0]*n, [0]*n
for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == 'C':
            h[i] += 1
            c[j] += 1  
res = 0
for i in h:
    res += i*(i-1) //2
for i in c:
    res += i*(i-1) //2
print(res)