letters = ["a", "b", "c"]
letters.append("d")
letters.extend(["e", "f"])
letters.insert(2, "v")
print(letters)

letters.remove("e")
letters.pop(0)
del letters   #deleted the object
print(letters)  #throws error