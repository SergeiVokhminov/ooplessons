class Product:
    """Класс продуктов."""

    name: str
    description: str
    price: float | int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    user_prod = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    user_prod1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    user_prod2 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    print(user_prod.name)
    print(user_prod.description)
    print(user_prod.price)
    print(user_prod.quantity)
    print()
    print(user_prod1.name)
    print(user_prod1.description)
    print(user_prod1.price)
    print(user_prod1.quantity)
    print()
    print(user_prod2.name)
    print(user_prod2.description)
    print(user_prod2.price)
    print(user_prod2.quantity)
