class Point:
    def draw(self):
        print("drawing")

point = Point()
point.draw()
print(type(point))
print(isinstance(point, Point))