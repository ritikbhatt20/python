class Animal:
    def __init__(self):
        self.age = 45

    def eat(self):
        print("eat")

#Animal: Parent class
#Mammal: Child class
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

tiger = Mammal()
print(tiger.age)
tiger.eat()