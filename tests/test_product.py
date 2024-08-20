def test_product_init(first_product, second_product):
    assert first_product.name == "Iphone 15"
    assert first_product.description == "512GB, Gray space"
    assert first_product.price == 210000.0
    assert first_product.quantity == 8
    assert second_product.name == "Iphone 14"
    assert second_product.description == "256GB, Blue space"
    assert second_product.price == 160000
    assert second_product.quantity == 6


def test_product_none_name(product_none_name):
    assert product_none_name.name == ""
    assert product_none_name.description == "Фоновая подсветка"
    assert product_none_name.price == 123000.0
    assert product_none_name.quantity == 7


def test_product_name(product_name):
    assert product_name == "Samsung Galaxy C23 Ultra"


def test_product_price_(product_price):
    assert product_price == 123000.0
