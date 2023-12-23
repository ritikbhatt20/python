x = 10
print(id(x)) #gives the address of the memory location
x = 20
print(id(x))
tup = (1, 2, 3, 4, 5, 5)
print(tup)
# since integers are immutable, their value cannot be changed at the same memory address
# lists are mutable, their value can be changed and mery address remains the same