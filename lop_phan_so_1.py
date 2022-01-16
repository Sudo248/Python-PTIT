import math
class PhanSo:
    def __init__(self, tu, mau) -> None:
        self.tu = tu
        self.mau = mau
    
    def to_string(self):
        uc = math.gcd(self.tu, self.mau)
        if self.tu % uc == 0: self.tu //= uc
        if self.mau % uc == 0: self.mau //= uc

        # if self.mau == 1: return self.tu
        return "{}/{}".format(self.tu,self.mau)

a,b = map(int,input().split())
ps = PhanSo(a,b)
print(ps.to_string())