class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def stud(self):
        print("I am Student")

stud1 = Student("abc", 18, 91)

stud1.display()
stud1.stud()
print(stud1.marks)
