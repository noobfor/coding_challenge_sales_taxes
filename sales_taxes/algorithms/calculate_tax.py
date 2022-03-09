from math import ceil
from sales_taxes.product import ProductType


def round_up_to_005(n):
    return ceil(n*20) / 20


def calculate_tax_for_product(product):
    """
    Calculates the tax for a given product

    :param product: Given Product defined by their name, price, type and imported or not
    :return:
            price_tax: The end price after adding all taxes to the price
            overall_tax: Overall taxes needed to pay
    """
    overall_tax = 0
    basic_tax = 0
    # check what type of product
    if product.product_type == ProductType.OTHER:
        # calc basic tax if not exception
        basic_tax = round_up_to_005((10*product.price)/100)
        overall_tax += basic_tax
    # check if imported or not
    if product.imported:
        new_price = basic_tax + product.price
        import_tax = round_up_to_005((5*product.price)/100)
        price_tax = round(new_price + import_tax, 2)
        overall_tax += import_tax

        return price_tax, overall_tax
    else:
        price_tax = round(product.price + basic_tax, 2)
        return price_tax, overall_tax
