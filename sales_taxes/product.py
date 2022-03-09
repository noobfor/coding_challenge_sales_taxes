from enum import Enum


class ProductType(Enum):
    BOOK = 1
    FOOD = 2
    MEDICAL = 3
    OTHER = 4


class Product:

    def __init__(self, name, price, product_type: ProductType, imported):
        self.name = name
        self.price = price
        # TODO: check if product type is one of the possible cases otherwise return error
        self.product_type = product_type
        self.imported = imported
