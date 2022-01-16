class Tram:
    ID = 1
    def __init__(self, name):
        self.id = Tram.ID
        Tram.ID += 1
        self.name = name
        self.time = 0
        self.amount = 0
        
    def addTime(self, begin, end):
        begin = [int(i) for i in begin.split(":")]
        end = [int(i) for i in end.split(":")]
        self.time += end[1]-begin[1] if begin[0] == end[0] else (end[0]-begin[0]-1)*60 + end[1] + (60 - begin[1])

    def addAmount(self, amount):
        self.amount += int(amount)
    
    def calAvg(self):
        return self.amount / (self.time / 60)
    
    def to_string(self):
        return "T%02d %s %.2f" % (self.id, self.name, self.calAvg())

if __name__ == "__main__":
    listTram = []
    n = int(input())
    def getIndex(name):
        for i in range(len(listTram)):
            if listTram[i].name == name:
                return i
        return -1

    while n > 0:
        n-=1
        name = input()
        begin = input()
        end = input()
        amount = input()

        index = getIndex(name)
        if index == -1:
            listTram.append(Tram(name))
        listTram[index].addTime(begin, end)
        listTram[index].addAmount(amount)
    
    for i in listTram:
        print(i.to_string())
        



        
