from typing import Any

from src.category import Category
from src.product import Product


def test_category_init(first_category: Any, second_category: Any, category: Any) -> Any:
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert first_category.category_count == 3

    assert second_category.name == "Смартфоны"
    assert (
        second_category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert second_category.category_count == 3

    assert category.name == "Телевизоры"
    assert category.description == "Фоновая подсветка"
    assert Category.category_count == 3
    assert Category.product_count == 5


def test_category_product_none(category_product_none: Any) -> Any:
    assert category_product_none.name == "Телевизоры"
    assert category_product_none.description == "Фоновая подсветка"
    assert len(category_product_none.products) == 0


def test_product_price(first_product: Any, capsys: Any) -> Any:
    first_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_str_products(category: Any) -> Any:
    product3 = Product('55" FullHD', "Smart TV", 103000.0, 5)
    category.add_product(product3)
    assert category.products == (
        '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
        '50" QLED, 113000.0 руб. Остаток: 3 шт.\n'
        '55" FullHD, 103000.0 руб. Остаток: 5 шт.\n'
    )


def test_str_category(second_category):
    assert str(second_category) == "Смартфоны, количество продуктов: 13 шт."
