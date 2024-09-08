import pytest


def test_lawn_glass_init(lawn_grass1):
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"


def test_smartphone_add(lawn_grass1, lawn_grass2):
    assert lawn_grass1 + lawn_grass2 == 1000.0


def test_smartphone_add_not_smartphone(lawn_grass1, smartphone1):
    with pytest.raises(TypeError):
        lawn_grass1 + smartphone1
