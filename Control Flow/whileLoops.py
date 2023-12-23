number = 100
while number > 0:
    print(number)
    number = number // 2

word = "lettersnjngjnj"
values = {}
for letter in word:
    if letter in values:
        values[letter] = values.get(letter) + 1
    else:
        values[letter] = 1

print(values)
# print(values["u"])