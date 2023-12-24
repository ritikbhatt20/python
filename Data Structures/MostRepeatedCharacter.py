sentence = "This is a common interview question"
frequency = {}
for letter in sentence:
    if letter in frequency:
        frequency[letter] = frequency[letter] + 1

    else:
        frequency[letter] = 1

print(frequency)
max = 0
for item in frequency:
    if frequency.get(item) > max:
        max = frequency.get(item)
        char = item

print("The most repeated character is", char)