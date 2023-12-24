point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 30
print(point)

print(point.get("a"))
del point["x"]
point.pop("y")
print(point)