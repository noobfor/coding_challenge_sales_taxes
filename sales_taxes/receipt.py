from sales_taxes.algorithms.calculate_tax import calculate_tax_for_product, calculate_tax_for_list


class Receipt:
    def __init__(self):
        self.product_list = list()

    def add_product(self, product):
        self.product_list.append(product)

    def print_list(self):
        currentlist = self.product_list
        for product in currentlist:
            # TODO: calculate tax for product

            currenttax = calculate_tax_for_product(product)

            print(currentlist[product.name] + ":" + " ")
