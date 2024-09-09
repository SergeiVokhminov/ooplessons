from typing import Any

from src.product import Product


class Category:
    """Класс категории продуктов."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None) -> None:
        self.name = name
        self.description = description
        #  Сделали атрибут приватным.
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        tot_quantity = 0
        for i in self.__products:
            tot_quantity += i.quantity
        return f"{self.name}, количество продуктов: {tot_quantity} шт."

    #  Создаем атрибут как геттер (используя декоратор). Позволяет обращаться к методу, как атрибуту класса.
    #  Данный атрибут будет возвращать строку.
    @property
    def products(self) -> str:
        """Вывод списка товаров из приватного атрибута."""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    def add_product(self, new_product: Product) -> Any:
        """Добавление товаров и запись в приватный атрибут списка товаров."""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        try:
            total_price = 0
            total_quantity = 0
            for product in self.__products:
                total_price += product.price * product.quantity
                total_quantity += product.quantity
            full_price = total_price / total_quantity
        except ZeroDivisionError:
            return 0
        else:
            return round(full_price, 2)


if __name__ == "__main__":
    products1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 6)
    products2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    products3 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    print(str(products1))
    print(str(products2))
    print(str(products3))
    print()

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получение дополнительных функций для удобства жизни",
        [products1, products2],
    )

    print(str(category1))

    print(category1.name)
    print(category1.description)
    print(category1.products)
    print(category1.category_count)
    print(category1.product_count)
    print()

    category2 = Category("Телевизоры", "Фоновая подсветка", [products3])

    print(str(category2))

    print(category2.name)
    print(category2.description)
    print(category2.products)
    print(category2.category_count)
    print(category2.product_count)
    print()

    products4 = Product('55" QLED 4K', "Smart TV", 101000.0, 3)
    category2.add_product(products4)

    print(category2.products)
    print(category2.product_count)
    print(category2.category_count)
