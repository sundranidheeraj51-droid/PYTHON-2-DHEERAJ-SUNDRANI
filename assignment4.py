class Student:
    def get_data(self):
        self.name = input("Enter name: ")
        self.roll = int(input("Enter roll number: "))
        self.marks = int(input("Enter marks: "))

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Marks:", self.marks)
        print("Total Marks:", self.marks)
        print("Average Marks:", self.marks)

s1 = Student()
s1.get_data()
s1.display()