from sales_taxes.algorithms.calculate_tax import calculate_tax_for_product


class Receipt:
    def __init__(self):
        self.product_list = list()

    def add_product(self, product):
        self.product_list.append(product)

    def print_list(self):
        """
        Prints the receipt in the format:
        1 [name of product]: [price+tax]
        ...
        Sales Taxes: [Overall taxes]
        Total: [Total Price+Taxes]

        :return: void
        """
        current_list = self.product_list
        overall_taxes = 0
        overall_cost = 0
        for product in current_list:
            current_price_and_tax, overall_tax = calculate_tax_for_product(product)

            overall_taxes += overall_tax
            overall_cost += current_price_and_tax

            print("1 " + product.name + ": " + str(current_price_and_tax))

        print("Sales Taxes: " + str(round(overall_taxes, 2)))
        print("Total: " + str(round(overall_cost, 2)), end='\n\n')
