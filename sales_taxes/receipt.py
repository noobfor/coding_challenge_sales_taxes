class Receipt():
    def __init__(self):
        self.product_list = list()


    def add_product(self, product):
        self.product_list.append(product)


    def print_list(self):
        currentlist = self.product_list
        for product in currentlist:
            # TODO: calculate tax for product
            print(currentlist[product.name] + ":" + " ")
