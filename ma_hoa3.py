def sum(str):
    res = 0
    for i in str:
        res += ord(i) - ord('A')
    return res
def rol(str, tmp):
    res = ""
    for i in str:
        res = res + chr((ord(i)-ord('A') + tmp) % 26 + ord('A'))
    return res
t = int(input())
while t > 0:
    t -= 1
    s = input()
    n = len(s)
    s1 = s[:n//2]
    s2 = s[n//2:]
    s1 = rol(s1, sum(s1))
    s2 = rol(s2, sum(s2))
    res = ""
    for i in range(n//2):
        res = res + chr((ord(s1[i])-ord('A') + ord(s2[i])-ord('A'))%26 + ord('A'))
    print(res)