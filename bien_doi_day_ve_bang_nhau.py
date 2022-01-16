n = int(input())
a = [int(i) for i in input().split()]
Min = 10**10
res = 0
for i in a:
    x = 0
    for j in a:
        x += abs(i-j)
    if x < Min:
        Min = x
        res = i
print(Min, res)