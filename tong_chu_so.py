s = input()
res = 0
while len(s) > 1:
    res += 1
    sum = 0
    for i in s: sum += ord(i) - ord('0')
    s = str(sum)
print(res)

