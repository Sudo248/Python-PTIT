n = int(input())
a = [float(i) for i in input().split()]
res = 0.0
Max = max(a)
Min = min(a)
dem = 0
for i in a:
    if i != Max and i != Min: 
        res += i
        dem += 1

print(format(res/dem,".2f"))