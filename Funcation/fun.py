class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working")

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name) 
        self.department = department

    def work(self): 
        print(f"{self.name} is managing the {self.department} department")

def show_work(emp):
    emp.work() 

e1 = Employee("Alice")
m1 = Manager("Bob", "Sales")

show_work(e1)
show_work(m1)
