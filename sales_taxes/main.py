from sales_taxes.receipt import Receipt
from sales_taxes.product import Product, ProductType


def main():
    # Input 1
    book = Product("book", 12.49, ProductType.BOOK, False)
    music_CD = Product("music CD", 14.99, ProductType.OTHER, False)
    chocolate_bar = Product("chocolate bar", 0.85, ProductType.FOOD, False)

    receipt_1 = Receipt()
    receipt_1.add_product(book)
    receipt_1.add_product(music_CD)
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

    # TODO: add waiting for additional input of more products for a new receipt


if __name__ == '__main__':
    main()

