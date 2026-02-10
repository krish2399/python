class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannont be zero or nagative")
        self._price = value


product = Product(-10)
print(product.price)
