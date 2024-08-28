from src.category import Category
from src.product import Product

# class Iterator:
#
#     def __init__(self):
#         self.index = 0
#         pass
#
#     def __iter__(self):
#         pass
#
#     def __next__(self):
#         if self.index < len(self.)
#         pass


if __name__ == "__main__":
    products1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    products2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    products3 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    print(str(products1))
    print(str(products2))
    print(str(products3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получение дополнительных функций для удобства жизни",
        [products1, products2],
    )

    iter
