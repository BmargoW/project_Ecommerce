import pytest
from src.main import Product, Category, Smartphone, LawnGrass, PrintMixin


@pytest.fixture
def product_1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )

@pytest.fixture
def category_1(product_1):
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации,\
        но и получения дополнительных функций для удобства жизни", [product_1])


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )


@pytest.fixture
def grass_1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )



def test_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.quantity == 5
    assert product_1.price == 180000.0


def test_init_smartphone(smartphone_1):
    assert smartphone_1.efficiency == 90.3
    assert smartphone_1.model == "Note 11"
    assert smartphone_1.memory == 1024
    assert smartphone_1.color == "Синий"



def test_init_lawngrass(grass_1):
    assert grass_1.country == "Россия"
    assert grass_1.germination_period == "7 дней"
    assert grass_1.color == "Зеленый"


def test_str_product(product_1):
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product(product_1):
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert (product_1 + product2) == 2580000.0


def test_negative_add_product(smartphone_1, grass_1):
    with pytest.raises(TypeError):
        smartphone_1 + grass_1


def test_init_category(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == ("Смартфоны, как средство не только коммуникации,\
        но и получения дополнительных функций для удобства жизни")
    assert (
        category_1.products
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    )
    assert len(category_1.products) == 55
    assert category_1.category_count == 1
    assert category_1.product_count == 1


def test_str_category(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 5"


def test_category_products_property(category_1):
    assert (
        category_1.products
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    )


def test_category_add_product(category_1):
    product_4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category_1.add_product(product_4)
    assert category_1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
    )
    with pytest.raises(TypeError):
        category_1.add_product("Not a product")


def test_product_price_property(product_1):
    assert product_1.price == 180000.0


def test_product_price_setter_positive(product_1):
    new_price = 800
    product_1.price = new_price
    assert product_1.price == 800


def test_product_price_setter_negative(product_1):
    new_price = 0
    product_1.price = new_price
    assert product_1.price == 180000.0


def test_product_new_product():
    new_product_1 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product_1.name == "Samsung Galaxy S23 Ultra"
