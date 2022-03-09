from sales_taxes.receipt import Receipt
from sales_taxes.product import Product, ProductType


def main():
    # Input 1
    book = Product("book", 12.49, ProductType.BOOK, False)
    music_cd = Product("music CD", 14.99, ProductType.OTHER, False)
    chocolate_bar = Product("chocolate bar", 0.85, ProductType.FOOD, False)

    receipt_1 = Receipt()
    receipt_1.add_product(book)
    receipt_1.add_product(music_cd)
    receipt_1.add_product(chocolate_bar)
    receipt_1.print_list()

    # Input 2
    imported_chocolate = Product("imported box of chocolates", 10, ProductType.FOOD, True)
    imported_perfume = Product("imported bottle of perfume", 47.5, ProductType.OTHER, True)

    receipt_2 = Receipt()
    receipt_2.add_product(imported_chocolate)
    receipt_2.add_product(imported_perfume)
    receipt_2.print_list()

    # Input 3
    imported_perfume_2 = Product("imported bottle of perfume", 27.99, ProductType.OTHER, True)
    perfume = Product("bottle of perfume", 18.99, ProductType.OTHER, False)
    headache_pills = Product("packet of headache pills", 9.75, ProductType.MEDICAL, False)
    imported_chocolate_2 = Product("box of imported chocolates", 11.25, ProductType.FOOD, True)

    receipt_3 = Receipt()
    receipt_3.add_product(imported_perfume_2)
    receipt_3.add_product(perfume)
    receipt_3.add_product(headache_pills)
    receipt_3.add_product(imported_chocolate_2)
    receipt_3.print_list()

    add_new_receipt = "y"

    while not add_new_receipt == "n":

        new_product = None
        end_loop = ""
        new_receipt = Receipt()
        while not end_loop == "n":

            # TODO: check for invalid inputs
            product_name = input("Starting new receipt now, type the name of the product...")
            product_price = input("Type the price of the product...")
            product_type = int(input("Type the number for the type of the Product chosen from "
                                     "[1 = BOOK, 2 = FOOD, 3 = MEDICAL, 4 = OTHER]..."))
            product_imported = input("Is the product imported? y/n")
            if product_imported == "y":
                new_product = Product(product_name, float(product_price), ProductType(product_type), True)
            elif product_imported == "n":
                new_product = Product(product_name, float(product_price), ProductType(product_type), False)

            new_receipt.add_product(new_product)

            end_loop = input("Add another product? y/n")

        new_receipt.print_list()
        add_new_receipt = input("Create a new receipt? y/n")

    end_program = input("waiting for input to end program...")


if __name__ == '__main__':
    main()

