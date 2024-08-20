import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_none_name():
    return Product("", "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def product_name():
    return "Samsung Galaxy C23 Ultra"


@pytest.fixture
def product_price():
    return 123000.0


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        products=[
            ("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        products=[
            ("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            ("Iphone 15", "512GB, Gray space", 210000.0, 8)
        ]
    )


@pytest.fixture
def category_product_none():
    return Category(
        name="Телевизоры",
        description="Фоновая подсветка",
        products=None
    )
