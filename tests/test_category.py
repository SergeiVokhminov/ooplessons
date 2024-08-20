def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert len(first_category.products) == 1

    assert second_category.name == "Смартфоны"
    assert second_category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert len(second_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3


def test_category_product_none(category_product_none):
    assert category_product_none.name == "Телевизоры"
    assert category_product_none.description == "Фоновая подсветка"
    assert len(category_product_none.products) == 0
