conver = {
    "000": 0,
    "001": 1,
    "010": 2,
    "011": 3,
    "100": 4,
    "101": 5,
    "110": 6,
    "111": 7
}
s = input()
while len(s) % 3 != 0: s = '0' + s
for i in range(0,len(s),3):
    print(conver[s[i:i+3]],end='')