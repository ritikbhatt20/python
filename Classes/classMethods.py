class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod   #this is called decorator similar to annotation
    def zero(cls):     #this cls references to the class
        return cls (0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
point.draw()