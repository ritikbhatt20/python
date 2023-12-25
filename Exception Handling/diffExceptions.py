try:
    age = int(input("Enter your age: "))
    xfactor = 10 / age

except (ValueError, ZeroDivisionError) as e:
    print("You didn't enter a valid age")
    print(e)
    print(type(e))

else:
    print("You didn't throw any exception")

finally:   #this finally is always executed
    # file.close() 
    pass 