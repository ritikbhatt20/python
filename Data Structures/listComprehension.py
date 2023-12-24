items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = [item[1] for item in items]   #alternative for map fn
print(prices)

filtered = [item for item in items if item[1]>=10]     #alternative for map fn
print(filtered)