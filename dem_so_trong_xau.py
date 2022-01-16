t = int(input())
while t:
    t -= 1
    s = input()
    n = input()
    lenght = len(n)
    dem = 0
    i = 0
    while i <= len(s) - lenght:
        if s[i:i+lenght] == n:
            dem += 1
            i += lenght-1
        i += 1
    print(dem)
