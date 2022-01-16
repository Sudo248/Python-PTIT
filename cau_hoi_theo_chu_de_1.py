n = int(input())
res = {}
tmp = []
while n > 0:
    n -= 1
    s = input()
    if s == " " or s == "":
        res[tmp[0]] = len(tmp)-1
        tmp = []
    else:
        tmp.append(s)
        # if tmp[0] not in res:
        #     res[tmp[0]] = len(tmp)-1
        # else:
        #     res[tmp[0]] += len(tmp)-1
        
if len(tmp) > 1:
    res[tmp[0]] = len(tmp)-1
for k,v in res.items():
    print(f"{k}: {v}")
