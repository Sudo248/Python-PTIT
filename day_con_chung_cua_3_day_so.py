t = int(input())
while t:
    t -= 1
    A,B,C = map(int,input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    ok = True
    ia = ib = ic = 0
    while ia < A and ib < B and ic < C:
        if a[ia] == b[ib] == c[ic]:
            print(a[ia],end=" ")
            ia, ib, ic = ia+1, ib+1, ic+1
            ok = False
        elif a[ia] < b[ib]: ia += 1
        elif b[ib] < c[ic]: ib += 1
        else: ic += 1
    if ok: print("NO",end='')
    print()

        