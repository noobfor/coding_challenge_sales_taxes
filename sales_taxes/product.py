from enum import Enum


class ProductType(Enum):
    BOOK = 1
    FOOD = 2
    MEDICAL = 3
    OTHER = 4


class Product:

    def __init__(self, name, price, product_type: ProductType, imported):
        """
        Represents a product with the given attributes
        :param name: String name of the product
        :param price: Float price of the product
        :param product_type: product type of one of these types: BOOK, FOOD, MEDICAL, OTHER
        :param imported: boolean if the product is imported or not
        """
        self.name = name
        self.price = price
        if isinstance(product_type, ProductType):
            self.product_type = product_type
        else:
            raise AttributeError
        self.imported = imported
