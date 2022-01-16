s = input()
check = True
n = len(s)
for i in range(n):
    if s[i] != '6' and s[i] != '8': 
        check = False
        break
if check == False:
    print("NO")
else:
    for i in range(0, len(s)-2):
        if (int(s[i]) + int(s[i+1]) + int(s[i+2])  >= 24): 
            check = False
            break
    if check: print("YES")
    else: print("NO")