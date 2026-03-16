import pytest
from src.main import Product, Category


@pytest.fixture
def product_1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def category_1(product_1):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,\
        но и получения дополнительных функций для удобства жизни",
        [product_1]
    )


def test_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.quantity == 5
    assert product_1.price == 180000.0


def test_init_category(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == ("Смартфоны, как средство не только коммуникации,\
        но и получения дополнительных функций для удобства жизни")
    assert category_1.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. 5 шт.\n"
    assert len(category_1.products) == 46
    assert category_1.category_count == 1
    assert category_1.product_count == 1

def test_category_products_property(category_1):
    assert category_1.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. 5 шт.\n"

def test_category_add_product(category_1):
    product_4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category_1.add_product(product_4)
    assert category_1.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. 5 шт.\n'
 '55" QLED 4K, 123000.0 руб. 7 шт.\n')