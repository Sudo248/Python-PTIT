
import math
import re
def so_phong_phu(n):
    s = 0
    for i in range(2, int(math.sqrt(n)+1)):
        if(n % i == 0):
            j = n // i
            if i != j:
                s += i + j
            else:
                s += i
    return s+1 > n

def is_doi_xung(s):
    return s == s[::-1]

def tong_tich(*arg):
    tich = 1
    tong = 0
    for i in arg:
        tong += i
        tich *= i
    return tong, tich

s = """The most familiar palindromes in English 
are character-unit palindromes. The characters read 
the same backward as forward. Some examples of 
palindromic words are redivider, deified, civic, 
radar, level, rotor, kayak, reviver, racecar, 
madam, and refer. """

Max = ""
imax = 0
for i in re.split('[\\s\\.\\,\\n]+',s):
    if is_doi_xung(i):
        if imax < len(i):
            Max = i
            imax = len(i)


def noi(**arg):
    s = ""
    for i in arg:
        s += arg[i] + ' '
    return s[:-1]

print(noi(arg1="Welcome", arg2 = "To", arg3 = "Python"))

def giai_pt(a,b):
    if a == 0:
        if b == 0:
            print('pt co vo so nghiem')
        else: print('pt vo nghiem')
    else: print('pt co nghiem',-b/a)

giai_pt(2,3)