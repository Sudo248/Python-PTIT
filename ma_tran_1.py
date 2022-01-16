n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
k = int(input())

top, bot = 0,0
for i in range(n):
    for j in range(i+1,n):
        top += a[i][j]

for i in range(n):
    for j in range(i):
        bot += a[i][j]

m = abs(top - bot)
print("YES" if m <= k else "NO")
print(m)