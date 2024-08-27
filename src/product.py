from typing import Any
# from src.category import Category


class Product:
    """Класс продуктов."""

    name: str
    description: str
    price: float | int
    quantity: int

    def __init__(self, name: str, description: str, price: int | float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, new_product: dict) -> Any:
        name = new_product.get("name")
        description = new_product.get("description")
        price = new_product.get("price")
        quantity = new_product.get("quantity")

        return cls(name, description, price, quantity)

    @property
    def price(self) -> int | float:
        return self.__price

    @price.setter
    def price(self, new_price: Any) -> Any:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_answer = input(
                "Подтвердите изменение цены!\n" "Для подтверждения введите: y\n" "Для отмены введите: n\n"
            ).lower()
            if user_answer == "y":
                self.__price = new_price
            elif user_answer == "n":
                self.__price = self.__price
        else:
            self.__price = new_price


if __name__ == "__main__":
    prod1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    prod2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    prod3 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    print(prod1.name)
    print(prod1.description)
    print(prod1.price)
    print(prod1.quantity)
    print()
    print(prod2.name)
    print(prod2.description)
    print(prod2.price)
    print(prod2.quantity)
    print()
    print(prod3.name)
    print(prod3.description)
    print(prod3.price)
    print(prod3.quantity)
    print()
    prod4 = Product.new_product({"name": '43" FullHD', "description": "Смарт ТВ", "price": 43000.0, "quantity": 5})
    print(prod4.name)
    print(prod4.description)
    print(prod4.price)
    print(prod4.quantity)
    prod5 = Product.new_product({"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 2})
    print(prod5.quantity)

