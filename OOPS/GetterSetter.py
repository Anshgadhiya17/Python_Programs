class Product:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price

p = Product(float(input("Enter price: ")))

print("Current Price:", p.get_price())

new_price = float(input("Enter new price: "))
p.set_price(new_price)

print("Updated Price:", p.get_price())
