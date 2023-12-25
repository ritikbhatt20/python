try:
    age = int(input("Enter your age: "))

except ValueError as e:
    print("you didn't enter a valid age")
    print(e)
    print(type(e))

else:
    print("You didn't throw any exception")