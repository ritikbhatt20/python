class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 45

    def eat(self):
        print("eat")

#Animal: Parent class
#Mammal: Child class
class Mammal(Animal):
    def __init__(self):
        super().__init__()   #this super keyword calls the parent class
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")

m = Mammal()
# print(m.age)    #the constructor of mammal class (child) completely overrides const of animal class(parent)
print(m.age)
print(m.weight)