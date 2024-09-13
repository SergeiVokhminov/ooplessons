# Курс ООП (объектно-ориентированное программирование)

## Описание проекта:

В данном проекте реализуется объектно-ориентированное программирование.

## Модули проекта:

В проекте реализованы следующие модули:
1. category.py - содержит класс категории продуктов. список товаров сделан приватным атрибутом. реализован специальный метод add_product(), магический метод str
2. product.py - содержит класс продуктов. создан класс-метод new_product. цена товара сделана приватным атрибутом. описаны геттеры и сеттеры. реализованы магические методы str и add
3. utils.py - содержит функцию для чтения JSON-файла.
4. main.py - выводит работу всех функций проекта.
5. smartphone.py - содержит класс smartphone наследник класса Product.
6. lawngrass.py - содержит класс lawngrass наследник класса Product.
7. base_product.py - содержит базовый абстрактный класс, который является родительским для классов продуктов. 
8. mixin.py - реализован класс-миксин, который при создании объекта распечатывает в консоль информацию о том, от какого класса и с какими параметрами был создан объект.

## Установленные зависимости:
- black==24.8.0
- certifi==2024.7.4
- charset-normalizer==3.3.2
- click==8.1.7
- coverage==7.6.1
- et-xmlfile==1.1.0
- flake8==7.1.1
- idna==3.7
- iniconfig==2.0.0
- isort==5.13.2
- mccabe==0.7.0
- mypy==1.11.1
- mypy-extensions==1.0.0
- numpy==2.1.0
- openpyxl==3.1.5
- packaging==24.1
- pandas==2.2.2
- pathspec==0.12.1
- platformdirs==4.2.2
- pluggy==1.5.0
- pycodestyle==2.12.1
- pyflakes==3.2.0
- pytest==8.3.2
- pytest-cov==5.0.0
- python-dateutil==2.9.0.post0
- pytz==2024.1
- requests==2.32.3
- six==1.16.0
- typing_extensions==4.12.2
- tzdata==2024.1
- urllib3==2.2.2

## Установка

1. Клонируйте репозиторий:
'''
git clone https://github.com/SergeiVokhminov/ooplessons.git
'''

2. Установите зависимости:
```
pip install -r requirements.txt
```

## Тестирование:

1. в проекте используется фреймворк тестирования "pytest".
2. для запуска тестов выполните команду: "pytest"
3. для просмотра покрытия тестов, выполните команду: pytest --cov

## Использование модуля main.py:

1. Откройте модуль
2. Запустите if __name__ == "__main__"

## Документация

Для получения дополнительной информации обратитесь к [документации](README.md)

## Лицензия
