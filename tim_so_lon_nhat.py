import re
t = int(input())
while t > 0:
    t -= 1
    s = input()
    a = [int(i) for i in re.findall('\d+', s)]
    print(max(a))
