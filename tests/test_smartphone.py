import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Iphone 15"
    assert smartphone1.description == "512GB, Gray space"
    assert smartphone1.price == 200000.0
    assert smartphone1.quantity == 8
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == "15"
    assert smartphone1.memory == 512
    assert smartphone1.color == "Gray space"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 400000.0


def test_smartphone_add_not_smartphone(smartphone1, lawn_grass1):
    with pytest.raises(TypeError):
        smartphone1 + lawn_grass1
