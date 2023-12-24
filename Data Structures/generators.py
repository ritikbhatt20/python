from sys import getsizeof

values = (x * 2 for x in range(1000000))
print(values)  #It will create a generator object

# Unlike lists, it won't store all the objects in memory
# It will generate and spit  a new value in each iteration
# for x in values:
#     print(x)

print("gen:", getsizeof(values))

values = [x * 2 for x in range(1000000)]
print("list:", getsizeof(values))


