import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def second_product():
    return Product("Iphone 14", "256GB, Blue space", 160000, 6)


@pytest.fixture
def third_product():
    return {"name": "Iphone 15pro", "description": "512GB", "price": 2160000, "quantity": 2}


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
        description="Смартфоны, как средство не только коммуникации, "
        "но и получение дополнительных функций для удобства жизни",
        products=[("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получение дополнительных функций для удобства жизни",
        products=[
            ("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            ("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def category_product_none():
    return Category(name="Телевизоры", description="Фоновая подсветка", products=None)


@pytest.fixture
def json_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
            "станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]
