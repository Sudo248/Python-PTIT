def is_even(n):
    while n > 0:
        if n % 2 != 0: return False
        n //= 10
    return True
a = []

for i in range(2,1000,2):
    if is_even(i):
        s = str(i)
        a.append(int(s + s[::-1]))

t = int(input())
while t:
    t -= 1
    n = int(input())
    for i in a:
        if i < n: print(i,end=' ')
        else: break
    print()