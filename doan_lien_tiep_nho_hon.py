t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    stack, res = [], [0]*n
    for i in range(n):
        while len(stack) > 0 and a[stack[-1]] <= a[i] :
            stack.pop()
        tmp = 0 if (len(stack) == 0) else stack[-1]+1
        tmp = i - tmp + 1
        res[i] = tmp
        stack.append(i)
    for i in res:
        print(i, end=' ')
    print()
