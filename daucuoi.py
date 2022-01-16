t = int(input())
while t:
    t-=1
    s = input()
    if s[:2] == s[-2:]:
        print("YES")
    else: 
        print("NO")
