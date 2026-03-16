
class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        elif new_price <= 0:
            self.__price = "Цена не должан быть нулевая или отрицательная"



    @classmethod
    def new_product(cls, my_dict):
        my_list = []
        for value in my_dict.values():
            my_list.append(value)
        name, description, price, quantity = my_list
        return  cls(name, description, price, quantity)


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

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products = ""
        for i in self.__products:
            products += f"{i.name}, {i.price} руб. {i.quantity} шт.\n"
        return products



if __name__ == "__main__":  # pragma no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
          {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
           "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)
    #
    new_product.price = 800
    print(new_product.price)
    #
    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)