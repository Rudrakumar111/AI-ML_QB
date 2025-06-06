class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_sound(animal):
    animal.speak()  

animals = [Dog(), Cat(), Animal()]

for a in animals:
    make_sound(a)
