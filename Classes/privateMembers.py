class TagCloud:
    def __init__(self):
        self.__tags = {}   #using fn + F2, renaming it as __tags and making it private

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count
    
    def __len__(self):
        return len(self.__tags)

cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("lol")
print(len(cloud))
print(cloud["python"])
print(cloud.__dict__)  # __dict__ holds all the attributes of the class
print(cloud._TagCloud__tags)