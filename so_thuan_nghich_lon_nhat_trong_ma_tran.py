
def thuan_nghich(n):
    if n < 10: return False
    n = str(n)
    return n == n[::-1]

n, m = map(int, input().split())
a = [[]]*n
for i in range(n):
    a[i] = [int(i) for i in input().split()]

MAX = 0
for i in a:
    for j in i:
        if thuan_nghich(j) and MAX < j:
            MAX = j
if MAX == 0:
    print("NOT FOUND")
else:
    print(MAX)
    for i in range(n):
        for j in range(m):
            if a[i][j] == MAX:
                print(f"Vi tri [{i}][{j}]")

