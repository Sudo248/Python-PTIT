def luy_thua(x,y):
    if x < 0 or y < 0:
        return 0
    if y == 1: return x
    res = luy_thua(x, y//2)
    if y % 2 == 0: return res*res
    else: return x*res*res
