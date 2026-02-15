class Demo:
    def __init__(self, value):
        self.__value = value

    def show(self):
        print("Value:", self.__value)

val = int(input("Enter value: "))
d = Demo(val)
d.show()
