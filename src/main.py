from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def scope_of_application(self):
        super().__init__()
        pass


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def scope_of_application(self):
        return print("Купля-продажа")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if issubclass(type(other), self.__class__):
            full_price = (self.__price * self.quantity) + (
                other.__price * other.quantity
            )
            return full_price
        raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        elif new_price <= 0:
            print("Цена не должан быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, my_dict):
        my_list = []
        for value in my_dict.values():
            my_list.append(value)
        name, description, price, quantity = my_list
        return cls(name, description, price, quantity)


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def scope_of_application(self):
        return print("Электроника")


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def scope_of_application(self):
        return print("Сельское и частное хозяйство")


class Category:
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products if products else [])

    def __str__(self):
        count = 0
        for i in self.__products:
            count += i.quantity
        return f"{self.name}, количество продуктов: {count}"

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products = ""
        for i in self.__products:
            products += f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n"
        return products

    def middle_price(self):
        try:
            a = 0
            for i in self.__products:
                a += i.price
            return a / len(self.__products)
        except ZeroDivisionError:
            return 0


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())