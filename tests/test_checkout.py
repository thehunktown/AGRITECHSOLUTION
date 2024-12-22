import unittest
from src.checkout import Checkout

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.pricing_rules = {
            'A': {'price': 50, 'discount': (3, 130)},
            'B': {'price': 30, 'discount': (2, 45)},
            'C': {'price': 20},
            'D': {'price': 15}
        }
        self.checkout = Checkout(self.pricing_rules)

    def test_empty_cart(self):
        self.assertEqual(self.checkout.calculate_total(), 0)

    def test_single_item(self):
        self.checkout.scan('A')
        self.assertEqual(self.checkout.calculate_total(), 50)

    def test_discounted_items(self):
        for _ in range(3):
            self.checkout.scan('A')
        self.assertEqual(self.checkout.calculate_total(), 130)

    def test_mixed_items(self):
        for item in "AAABBD":
            self.checkout.scan(item)
        self.assertEqual(self.checkout.calculate_total(), 190)

if __name__ == "__main__":
    unittest.main()
