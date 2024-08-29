from typing import Any

from src.product import Product


def test_product_init(first_product: Any, second_product: Any) -> Any:
    assert first_product.name == "Iphone 15"
    assert first_product.description == "512GB, Gray space"
    assert first_product.price == 210000.0
    assert first_product.quantity == 8
    assert second_product.name == "Iphone 14"
    assert second_product.description == "256GB, Blue space"
    assert second_product.price == 160000
    assert second_product.quantity == 6


def test_product_none_name(product_none_name: Any) -> Any:
    assert product_none_name.name == ""
    assert product_none_name.description == "Фоновая подсветка"
    assert product_none_name.price == 123000.0
    assert product_none_name.quantity == 7


def test_product_name(product_name: Any) -> Any:
    assert product_name == "Samsung Galaxy C23 Ultra"


def test_product_price(product_price: int | float) -> Any:
    assert product_price == 123000.0


def test_third_product(third_product: Any) -> Any:
    new_product = Product.new_product(third_product)
    assert new_product.name == "Iphone 15pro"
    assert new_product.description == "512GB"
    assert new_product.price == 2160000
    assert new_product.quantity == 2


def test_str_product(first_product):
    assert str(first_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_add_product(first_product, second_product):
    assert first_product + second_product == 2640000.0
