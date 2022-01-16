dem = 0
a = set()
while dem < 10:
    for i in input().split():
        dem += 1
        a.add(int(i)%42)
print(len(a)) 


