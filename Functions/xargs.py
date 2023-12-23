def multiply(*numbers):  # when we mark it with asterisk we can give multiple numbers in arg
    print(numbers)


multiply(2,3,4,5)

def mul(*numbers):
    total = 1
    for number in numbers:
        total = total * number
        return total

print(mul(2, 3, 4, 5))