# Person class (Base class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Employee class (inherits from Person)
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        # Call Person constructor
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_employee(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Manager class (inherits from Employee → and indirectly Person)
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        # Call Employee constructor
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def show_manager(self):
        print("Department:", self.department)


# Creating Manager object
m = Manager("Anand", 20, "E101", 50000, "IT")

# Calling methods from all classes
print("---- Person Details ----")
m.show_person()

print("\n---- Employee Details ----")
m.show_employee()

print("\n---- Manager Details ----")
m.show_manager()
