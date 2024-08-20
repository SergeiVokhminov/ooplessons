def test_product_init(product):
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_product_none_name(product_none_name):
    assert product_none_name.name == ""
    assert product_none_name.description == "Фоновая подсветка"
    assert product_none_name.price == 123000.0
    assert product_none_name.quantity == 7


def test_product_name(product_name):
    assert product_name == "Samsung Galaxy C23 Ultra"


def test_product_price_(product_price):
    assert product_price == 123000.0
