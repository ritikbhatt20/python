class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"point ({self.x}, {self.y})")

point = Point(3, 4)
print(point.x)
point.draw()
