n = int(input())
a = []
while len(a) < n:
    a.extend([int(i) for i in input().split()])
chan = []
le = []
for i in a:
    if i % 2 == 0: chan.append(i)
    else: le.append(i)
chan.sort()
le.sort(reverse=True)
i,j=0,0
for x in a:
    if x % 2 == 0:
        print(chan[i],end=' ')
        i += 1
    else:
        print(le[j],end=' ')
        j += 1