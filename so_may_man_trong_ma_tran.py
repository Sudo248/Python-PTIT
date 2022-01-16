
n, m = map(int, input().split())
a = [[]]*n
for i in range(n):
    a[i] = [int(i) for i in input().split()]

Min = min(min(i) for i in a)
Max = max(max(i) for i in a)
lucky = Max - Min
ok = False
for i in a:
    if lucky in i:
        ok = True
        break
if ok:
    print(lucky)
    for i in range(n):
        for j in range(m):
            if a[i][j] == lucky:
                print(f"Vi tri [{i}][{j}]")
else:
    print("NOT FOUND")
