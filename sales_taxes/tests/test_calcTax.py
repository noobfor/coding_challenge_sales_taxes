import unittest
from sales_taxes.product import Product, ProductType
from sales_taxes.algorithms import calculate_tax


class TestCalculateTax(unittest.TestCase):

    def test_other_product(self):

        other = Product("other", 14.99, ProductType.OTHER, False)

        self.assertEqual(calculate_tax.calculate_tax_for_product(other), 16.49)


# TODO: add testcases for different type of producttypes and check for error

if __name__ == '__main__':
    unittest.main()
