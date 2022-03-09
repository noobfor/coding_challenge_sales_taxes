import unittest
from sales_taxes.product import Product, ProductType
from sales_taxes.algorithms import calculate_tax


class TestCalculateTax(unittest.TestCase):

    def test_other_1(self):
        other = Product("other", 14.99, ProductType.OTHER, False)
        self.assertEqual(calculate_tax.calculate_tax_for_product(other)[0], 16.49)

    def test_other_2(self):
        other = Product("other", 18.99, ProductType.OTHER, False)
        self.assertEqual(calculate_tax.calculate_tax_for_product(other)[0], 20.89)

    def test_imported_other_1(self):
        other = Product("other", 47.50, ProductType.OTHER, True)
        self.assertEqual(calculate_tax.calculate_tax_for_product(other)[0], 54.65)

    def test_imported_other_2(self):
        other = Product("other", 27.99, ProductType.OTHER, True)
        self.assertEqual(calculate_tax.calculate_tax_for_product(other)[0], 32.19)

    def test_book(self):
        book = Product("book", 12.49, ProductType.BOOK, False)
        self.assertEqual(calculate_tax.calculate_tax_for_product(book)[0], 12.49)

    def test_food(self):
        food = Product("food", 0.85, ProductType.FOOD, False)
        self.assertEqual(calculate_tax.calculate_tax_for_product(food)[0], 0.85)

    def test_imported_food_1(self):
        food = Product("food", 10, ProductType.FOOD, True)
        self.assertEqual(calculate_tax.calculate_tax_for_product(food)[0], 10.5)

    def test_imported_food_2(self):
        food = Product("food", 11.25, ProductType.FOOD, True)
        self.assertEqual(calculate_tax.calculate_tax_for_product(food)[0], 11.85)

    def test_medical(self):
        medical = Product("medical", 9.75, ProductType.MEDICAL, False)
        self.assertEqual(calculate_tax.calculate_tax_for_product(medical)[0], 9.75)


# TODO: add testcases for different type of producttypes and check for error

if __name__ == '__main__':
    unittest.main()
