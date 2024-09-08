from src.product import Product


class Smartphone(Product):
    """ ."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.color = color
        self.efficiency = efficiency
        self.memory = memory
        self.model = model

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price + other.price
        else:
            raise TypeError


if __name__ == '__main__':
    smartphone1 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone2 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.color)
    print(smartphone1.efficiency)
    print(smartphone1.description)
    print(smartphone1.memory)
    print(smartphone1.model)
    print(smartphone1.price)
    print(smartphone1.quantity)

    print(smartphone1 + smartphone2)
