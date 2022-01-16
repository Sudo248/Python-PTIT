from itertools import permutations

s = list(input())
res = permutations(s)
for i in res:
    for j in i:
        print(j,end='')
    print()