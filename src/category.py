from src.product import Product


class Category:
    """Класс категории продуктов."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        #  Сделали атрибут приватным.
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    #  Создаем атрибут как геттер (используя декоратор). Позволяет обращаться к методу, как атрибуту класса.
    #  Данный атрибут будет возвращать строку.
    @property
    def products(self):
        """Вывод списка товаров из приватного атрибута."""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name} {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def add_product(self, new_product: Product):
        """Добавление товаров и запись в приватный атрибут списка товаров."""
        for product in self.__products:
            if product.name == new_product.name:
                product.quantity += new_product.quantity
                if product.price <= new_product.price:
                    product.price = new_product.price
                return

        else:
            self.__products.append(new_product)
            Category.product_count += 1
            return self.__products


if __name__ == "__main__":
    products1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    products2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    products3 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получение дополнительных функций для удобства жизни",
        [products1, products2],
    )

    print(category1.name)
    print(category1.description)
    print(category1.products)
    print(category1.category_count)
    print(category1.product_count)
    print()

    category2 = Category("Телевизоры", "Фоновая подсветка", [products3])

    print(category2.name)
    print(category2.description)
    print(category2.products)
    print(category2.category_count)
    print(category2.product_count)
    print()

    products4 = Product('45" QLED', "Фоновая подсветка", 101000.0, 3)
    category2.product = products4

    print(category2.products)
    print(category2.product_count)
    print(category2.category_count)
