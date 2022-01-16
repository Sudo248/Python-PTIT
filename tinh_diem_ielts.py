import math
bang_diem = {
    range(39, 41):9.0,
    range(37,39):8.5,
    range(35,37):8.0,
    range(33,35):7.5,
    range(30,33):7.0,
    range(27,30):6.5,
    range(23,27):6.0,
    range(20,23):5.5,
    range(16,20):5.0,
    range(13,16):4.5,
    range(10,13):4.0,
    range(7,10):3.5,
    range(5,7):3.0,
    range(3,5):2.5,
}

def my_round(n):
    s = [int(i) for i in str(n).split('.')]
    if s[1] in range(0,25):
        s[1] = 0
    elif s[1] in range(25,75):
        s[1] = 5
    else:
        s[0] += 1
        s[1] = 0
    return f"{s[0]}.{s[1]}"


def getMark(n):
    for i in bang_diem.keys():
        if n in i:
            return bang_diem.get(i)

n = int(input())
while n > 0:
    n -= 1
    inp = input().split()
    a = getMark(int(inp[0]))
    b = getMark(int(inp[1]))
    c = float(inp[2])
    d = float(inp[3])
    avg = round((a+b+c+d)/4,2)
    print(my_round(avg))