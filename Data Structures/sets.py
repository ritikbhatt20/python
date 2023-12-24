numbers = [1, 1, 2, 3, 4]
first = set(numbers)
first.add(6)
first.remove(2)
print(first)

second = {1, 5}
print(first | second)   #takes the union of sets
print(first & second)   #takes the intersection of sets
print(first - second)
print(first ^ second)   