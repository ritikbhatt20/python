class Product:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set_price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value


product = Product(50)
print(product.set_price(50))
