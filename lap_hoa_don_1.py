class HoaDon:
    ID = 1
    def __init__(self, name, old, new) -> None:
        self.id = HoaDon.ID 
        HoaDon.ID += 1
        self.name = name
        amount = new - old
        money = 0
        if amount > 100:
            money = 50 * 100
            money += 50 * 150
            money += (amount - 100) * 200
            money += money*0.05
        elif amount > 50:
            money = 50*100
            money += (amount - 50) * 150
            money += money * 0.03
        else: 
            money = amount * 100
            money += money * 0.02

        self.money = round(money)
    
    def to_string(self):
        return "KH%02d %s %d" % (self.id, self.name, self.money)

if __name__ == "__main__":
    n = int(input())
    listHD = []
    while n > 0:
        n -= 1
        listHD.append(HoaDon(input(), int(input()), int(input())))

    listHD.sort(key=lambda x: (-x.money, x.id))
    for i in listHD:
        print(i.to_string())