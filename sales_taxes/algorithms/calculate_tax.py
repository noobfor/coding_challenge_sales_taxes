from sales_taxes.product import ProductType


def calculate_tax_for_product(product):
    # check what type of product
    if product.product_type == ProductType.OTHER:
        # calc tax
        tax = (10*product.price)/100
        # check if imported or not
        if product.imported:
            # TODO: add imported tax
            return product.price
        else:
            return round(product.price+tax, 2)
    else:
        return product.price


def calculate_tax_for_list(product_list):
    pass
