from src.product import Product


class LawnGrass(Product):
    """Класс категории товаров. Наследник класса Product."""

    def __init__(
        self, name: str, description: str, price: int | float, quantity: int, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.color = color
        self.country = country
        self.germination_period = germination_period

    def __add__(self, other):
        """Сложение товаров только из одного класса продукта"""
        if type(other) is LawnGrass:
            return self.price + other.price
        else:
            raise TypeError


if __name__ == "__main__":
    lawn_grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    lawn_grass2 = LawnGrass("Газонная трава", "Элитная трава для газона", 300.0, 10, "Беларусь", "5 дней", "Красный")
    print(lawn_grass1.name)
    print(lawn_grass1.description)
    print(lawn_grass1.price)
    print(lawn_grass1.quantity)
    print(lawn_grass1.color)
    print(lawn_grass1.country)
    print(lawn_grass1.germination_period)

    print(lawn_grass1 + lawn_grass2)
    print(lawn_grass1 + "qrwq")
