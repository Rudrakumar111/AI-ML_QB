# Base class 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class 
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) 
        self.breed = breed      

    def speak(self):  
        print(f"{self.name} barks (Breed: {self.breed})")

d = Dog("Buddy", "Labrador")
d.speak()              
print(d.name)          
