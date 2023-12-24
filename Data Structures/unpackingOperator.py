numbers = [1, 2, 3, 4, 5, 6, 7]
x, y, z, *other = numbers
print(other)

values = list(range(5))
print(*values)   #unpacked all the numbers

values = [*range(5), *("Hello")]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z":4}   #for dict, double unpacking operator
print(combined)

