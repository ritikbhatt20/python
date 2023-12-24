numbers = [1, 2, 3, 4, 4, 4, 6, 7, 9]
# first, second, third = numbers   #list unpacking
# print(first, second, third)

first, second, *other = numbers    #list packing 
print(first, second)
print(other)

first, *other, last = numbers   
print(first, last)
print(other)
