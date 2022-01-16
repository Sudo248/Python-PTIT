class SoPhuc:
    def __init__(self, thuc, ao) -> None:
        self.thuc = thuc
        self.ao = ao
    
    def add(self, o):
        return SoPhuc(self.thuc + o.thuc, self.ao + o.ao)
    
    def mutil(self, o):
        return SoPhuc(self.thuc*o.thuc - self.ao*o.ao, self.thuc*o.ao + self.ao*o.thuc)
    
    def to_string(self):
        return "{} + {}i".format(self.thuc, self.ao) if self.ao > 0 else "{} - {}i".format(self.thuc, abs(self.ao))

n = int(input())

while n > 0:
    n -= 1
    a,b,c,d = map(int, input().split())
    sp1 = SoPhuc(a,b)
    sp2 = SoPhuc(c,d)
    sum = sp1.add(sp2)
    print(sp1.mutil(sum).to_string() + ", " + sum.mutil(sum).to_string())