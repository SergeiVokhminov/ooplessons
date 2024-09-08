import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """
    Функция чтения JSON-файла
    :param path: принимает JSON-файл.
    :return: Возвращает список словарей.
    """

    try:
        full_path = os.path.abspath(path)
        with open(full_path, "r", encoding="UTF-8") as f:
            data_file = json.load(f)
            return data_file
    except Exception:
        raise ValueError("Возникла ошибка при обработке файла!")


def create_json(data: list[dict]) -> list:
    """
    :param data:
    :return:
    """
    users_list = []
    for category in data:
        product_list = []
        for product in category["products"]:
            product_list.append(Product(**product))
        category["products"] = product_list
        users_list.append(Category(**category))

    return users_list


if __name__ == "__main__":
    user_file = read_json("../data/products.json")
    print(user_file)
    users_data = create_json(user_file)
    print()
    print(users_data)
    print(users_data[0].name)
    print(users_data[1].name)
