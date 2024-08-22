from src.product import Product


def test_category_init(first_category, second_category, category):
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
    assert (
        category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category.category_count == 3


def test_category_product_none(category_product_none):
    assert category_product_none.name == "Телевизоры"
    assert category_product_none.description == "Фоновая подсветка"
    assert len(category_product_none.products) == 0


def test_product_price(first_product, capsys):
    first_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_str_product(category):
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category.add_product(product)
    assert category.products == '55" QLED 4K, 123000.0 руб. Остаток: 14 шт.\n'
