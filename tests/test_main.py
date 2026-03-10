import pytest
from src.main import Product, Category


@pytest.fixture
def product_1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
        180000.0, 5
    )


@pytest.fixture
def category_1():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,\
        но и получения дополнительных функций для удобства жизни",
        ["product1", "product2", "product3"],
    )


def test_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.quantity == 5
    assert product_1.price == 180000.0


def test_init_category(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == ("Смартфоны, как средство \
    не только коммуникации,но \
    и получения дополнительных функций для удобства жизни")
    assert category_1.products == ["product1", "product2", "product3"]
    assert len(category_1.products) == 3
    assert category_1.category_count == 1
    assert category_1.product_count == 3
