from typing import Any
from unittest.mock import patch

import pytest

from src.utils import read_json, create_json


@patch("builtins.open")
def test_get_json_ok(open_mock: Any) -> Any:
    open_mock.return_value.__enter__.return_value.read.return_value = '[{"name": "test"}, {"name": "more"}]'
    assert read_json("any_path") == [{"name": "test"}, {"name": "more"}]


def test_json_error() -> None:
    with pytest.raises(ValueError) as ex:
        read_json("2352sds")
        assert str(ex.value) == "Возникла ошибка при обработке файла!"


def test_create_json_init(json_data):
    result = create_json(json_data)
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"
    assert (
        result[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert (
        result[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
