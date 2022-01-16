s = input()
a = 0
for i in s:
    if i.isupper():
        a += 1

if a > len(s)//2:
    print(s.upper())
else:
    print(s.lower())