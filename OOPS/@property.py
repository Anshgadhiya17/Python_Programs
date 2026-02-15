class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

l = float(input("Enter length: "))
w = float(input("Enter width: "))

r = Rectangle(l, w)
print("Area:", r.area)
