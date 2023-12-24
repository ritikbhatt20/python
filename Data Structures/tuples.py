point = (1, 2) + (3, 4)
point = (1, 2) * 3
print(point)
point = tuple([1, 2])
print(point)
point = (1, 2, 3)
print(point[0:2])
x, y, z = point   #unpacking the tuple
if 10 in point:
    print("exists")

# point[1] = 10   #it will throw an error