class Point:

    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(3, 4)
print(point.x)   #Here x and y are instance attributes... They can be diff for diff objects
point.draw()
print(point.default_color)
print(Point.default_color)   #def color is class attribute applicable to all objects of the class