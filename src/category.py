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
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


if __name__ == "__main__":
    products = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    products1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    products2 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    user_category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [products, products1],
    )
    user_category1 = Category("Телевизоры", "Фоновая подсветка", [products2])

    print(user_category.name)
    print(user_category.description)
    print(user_category.products)
    print()
    print(user_category1.name)
    print(user_category1.description)
    print(user_category1.products)
    print()
    print(user_category.category_count)
    print(user_category.product_count)
