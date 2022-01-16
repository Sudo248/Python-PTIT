import math

n = int(input())
a = [[]] * n
for i in range(n):
    a[i] = [int(i) for i in input().split()]

k = int(input())

sum_up = 0
sum_down = 0

for i in range(n):
    for j in range(n):
        if j < i:
            sum_up += a[i][j]
        if j > i:
            sum_down += a[i][j]
tmp = abs(sum_down-sum_up)
if tmp > k:
    print("NO")
else:
    print("YES")
print(tmp)