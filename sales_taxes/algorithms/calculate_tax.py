from math import ceil
from sales_taxes.product import ProductType


def round_up_to_005(n):
    return ceil(n*20) / 20


def calculate_tax_for_product(product):
    basictax = 0
    # check what type of product
    if product.product_type == ProductType.OTHER:
        # calc basic tax if not exception
        basictax = round_up_to_005((10*product.price)/100)

    # check if imported or not
    if product.imported:
        new_price = basictax + product.price
        import_tax = round_up_to_005((5*product.price)/100)
        return round(new_price + import_tax, 2)
    else:
        return round(product.price + basictax, 2)


def calculate_tax_for_list(product_list):
    pass
