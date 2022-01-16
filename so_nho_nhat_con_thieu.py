# n = int(input())
# a = set([int(i) for i in input().split()])
# x = 1
# for i in a:
#     if x != i:
#         break
#     x += 1
# print(x)

n = int(input())
a = sorted([int(i) for i in input().split()])
for i in range(n):
    if i == n - 1:
        print(a[i]+1)
        break
    if a[i] + 1 != a[i+1]:
        print(a[i]+1)
        break