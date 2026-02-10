class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)
class student(person):
    def __init__ (self,name,age,marks):
        super().__init__(name , age)
        self.marks = marks
    def stud(self):
        print("I am a student")


stud1=student("abc",18,92)
stud1.display()
stud1.stud()
stud1.marks=91
print(stud1.marks)