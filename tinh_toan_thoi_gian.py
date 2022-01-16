
class Game:
    def __init__(self, id, name, begin, end) -> None:
        self.id = id
        self.name = name
        
        b = [int(i) for i in begin.split(':')]
        e = [int(i) for i in end.split(':')]

        if e[0] == b[0]:
            self.time = e[1]-b[1]
        else:
            self.time = (e[0] - b[0] -1)*60 + 60 - b[1] + e[1]

    def to_string(self):
        return self.id + " " + self.name + " " + (str(self.time//60)+" gio ") + (str(self.time%60)+" phut")

t = int(input())
listG = []
while t > 0:
    t -= 1
    listG.append(Game(input(), input(), input(), input()))

listG.sort(key=lambda x: x.time, reverse=True)
for i in listG:
    print(i.to_string())