from ecommerce.shopping import sales

print("app initialized")

sales.calc_shipping()
sales.calc_tax()

print(dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)