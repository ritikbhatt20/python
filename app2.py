import constant
i=0
for i in range(0, 9):
    print(i)

print(constant.PI)
a = 5
print("the value of a is: ", a)
a = 20
b = 10
print("the value of a is {} an of b is {}".format(a,b))
add = a + 5
print("the sum value is %d" % add)
print(f"the value is {add}")
for i in range(1, 5):
    for j in range(i):
        print("#", end=" ")
    print()    
class my_class:
    pass
def function():
    pass
def sum(a, b):
    c=a+b
    return c

print(sum(6,88))
str = "Helloworld"
# print(str[:5])
print(str[1:5])