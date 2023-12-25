# every class inherits object class
class Animal(object):
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

m = Mammal()
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))
print(issubclass(Mammal, object))