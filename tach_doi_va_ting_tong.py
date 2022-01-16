n = int(input())
while n > 10:
    s = str(n)
    x = len(s)//2
    n = int(s[:x]) + int(s[x:])
    print(n)