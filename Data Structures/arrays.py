from array import array   # from array module, importing array class

numbers = array("i", [1, 2, 3])    #takes two arg, one the unicode character determining the type of values it would take
numbers.append(4)
numbers.pop()
numbers[0] = 2.34
print(numbers)