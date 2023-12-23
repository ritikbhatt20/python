def get_greet(first_name):
    return f"Hi {first_name}"


def greet(first_name):
    print(f"Hi {first_name}")

message = get_greet("Ritik")    
print(message)

file = open("content.txt", "w")
file.write(message)