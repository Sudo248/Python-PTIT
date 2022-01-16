from decimal import Decimal, ROUND_HALF_UP
class Student:
    ID = 1
    def __init__(self, name, marks) -> None:
        self.id = Student.ID
        Student.ID += 1
        self.name = name
        sumMarks = marks[0]+marks[1]
        for i in marks:
            sumMarks += i
        
        self.avg = Decimal(sumMarks) / Decimal(12)
        self.avg = self.avg.quantize(Decimal("0.1"), ROUND_HALF_UP)

    
    def rank(self):
        if self.avg >= 9.0: return "XUAT SAC"
        elif self.avg >= 8.0: return "GIOI"
        elif self.avg >= 7.0: return "KHA"
        elif self.avg >= 5.0: return "TB"
        else: return "YEU"
    
    def to_string(self):
        return f"HS{self.id:02d} {self.name} {self.avg} {self.rank()}"
    
if __name__ == "__main__":
    n = int(input())
    listStu = []
    while n > 0:
        n -= 1
        name = input()
        marks = [Decimal(i) for i in input().split()]
        listStu.append(Student(name, marks))
    
    listStu.sort(key=lambda x: (-x.avg, x.id))

    for i in listStu:
        print(i.to_string())
    
