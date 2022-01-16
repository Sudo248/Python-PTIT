t = int(input())
for test in range(t):
    t -= 1
    s1 = sorted(input())
    s2 = sorted(input())
    print("Test {}:".format(test+1),"YES" if s1 == s2 else "NO")