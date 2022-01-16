class Student:
    def __init__(self, name, ac, all) -> None:
        self.name = name
        self.ac = ac
        self.all = all
    def to_string(self):
        return f"{self.name} {self.ac} {self.all}"

n = int(input())
listST = []
while n>0:
    n -= 1
    name = input()
    ac, all = map(int, input().split())
    listST.append(Student(name, ac, all))
listST.sort(key=lambda x: (-x.ac, x.all, x.name))
for i in listST:
    print(i.to_string())
