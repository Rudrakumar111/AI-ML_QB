class Person:
    def __init__(self, name, age):
        self.name = name        
        self._age = age         
        self.__salary = 50000   

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount

class Employee(Person):
    def display_info(self):
        print(f"Name: {self.name}")      
        print(f"Age: {self._age}")        
        print(f"Salary: {self.get_salary()}")  


e = Employee("Ken", 30)
e.display_info()
e.set_salary(60000)
print("Updated Salary:", e.get_salary())
