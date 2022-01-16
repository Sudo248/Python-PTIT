import re
inp = ""

while True:
    try:
        s = input()
        inp += s
    except EOFError:
        break
inp = re.sub(r"\s+"," ", inp)
for i in re.split(r"[.?!] ?", inp):
    print(i.capitalize())
