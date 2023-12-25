class Text(str):   #inherits the built in type str
    def duplicate(self):
        return self + self
    
text = Text("Python")
print(text.upper())
print(text.duplicate())

class TrackableList(list):
    def append(self, object):
        print("Appending")
        super().append(object)

list = TrackableList()
list.append(12)