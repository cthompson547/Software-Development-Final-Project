python
class Product:
def __init__(self, name, price):
    self.name = name
    self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(Self, product):
        self.items.append(product)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def reset(self):
        self.items = []


menu = [
    Product("Rose Latte", 5.00),
    Product("Pink Hibiscus Tea", 4.00),
    Product("Espresso", 2.50),
    Product("Pink Rose cupcake", 2.00),
    Product("Matcha Latte", 3.00)
    Product("Blueberry Muffin" 1.50),
    Product("Crissant" 1.50),
    Product("Water" 2.00),
    Product("Panckaes" 4.00),
    Product("Breakfast sandwich", 2.50)
]