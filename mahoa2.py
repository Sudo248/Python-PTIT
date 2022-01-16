banMau = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    n = input()
    if n == "0":
        break
    n,s = n.split()
    n = int(n)
    s = s[::-1]
    for i in range(len(s)):
        for j in range(28):
            if s[i] == banMau[j]:
                print(banMau[((j+n)%28)],end="")
    print()


