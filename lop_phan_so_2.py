import math
class PhanSo:
    def __init__(self, tu, mau) -> None:
        self.tu = tu
        self.mau = mau
    
    def to_string(self):
        uc = math.gcd(self.tu, self.mau)
        if self.tu % uc == 0: self.tu //= uc
        if self.mau % uc == 0: self.mau //= uc
        return "{}/{}".format(self.tu,self.mau)

    def add(self, o):
        return PhanSo(self.tu*o.mau + self.mau*o.tu, self.mau*o.mau)
        

a,b,c,d = map(int,input().split())
ps1 = PhanSo(a,b)
ps2 = PhanSo(c,d)
print(ps1.add(ps2).to_string())