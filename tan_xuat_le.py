from typing import Counter


t = int(input())
while t:
    t -= 1
    n = int(input())
    b = Counter([int(i) for i in input().split()])
    for i in b:
        if b[i] % 2 != 0:
            print(i)
            break
