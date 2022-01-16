class Student:
    def __init__(self, name, dob, mark1, mark2, mark3) -> None:
        self.name = name
        self.dob = dob
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def to_string(self):
        return "%s %s %.1f" % (self.name, self.dob, self.mark1+self.mark2+self.mark3)

st = Student(input(), input(), float(input()), float(input()), float(input()))
print(st.to_string())