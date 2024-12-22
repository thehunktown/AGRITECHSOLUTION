class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.cart = {}

    def scan(self, item):
        if item not in self.cart:
            self.cart[item] = 0
        self.cart[item] += 1

    def calculate_total(self):
        total = 0
        for item, quantity in self.cart.items():
            if item in self.pricing_rules:
                unit_price = self.pricing_rules[item]['price']
                if 'discount' in self.pricing_rules[item]:
                    discount_quantity, discount_price = self.pricing_rules[item]['discount']
                    total += (quantity // discount_quantity) * discount_price
                    total += (quantity % discount_quantity) * unit_price
                else:
                    total += quantity * unit_price
        return total

if __name__ == "__main__":
    pricing_rules = {
        'A': {'price': 50, 'discount': (3, 130)},
        'B': {'price': 30, 'discount': (2, 45)},
        'C': {'price': 20},
        'D': {'price': 15}
    }
    checkout = Checkout(pricing_rules)
    items = input("Enter items scanned (e.g., 'ABCD'): ").strip()
    for item in items:
        checkout.scan(item)
    print(f"Total price: {checkout.calculate_total()}")
