app.py
from flask import Flask, render_template

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price



menu = {
    Product("Rose Latte", 5.00),
    Product("Pink Hibiscus Tea", 4.00),
    Product("Espresso", 2.50),
    Product("Pink Rose cupcake", 2.00),
    Product("Matcha Latte", 3.00),
    Product("Blueberry Muffin", 1.50),
    Product("Crissant", 1.50),
    Product("Water", 2.00),
    Product("Panckaes", 4.00),
    Product("Breakfast sandwich", 2.50),
    Product("Rose Latte", 5.00),
    Product("Pink Hibiscus Tea", 4.00),
    Product("Espresso", 2.50),
    Product("Pink Rose cupcake", 2.00),
    Product("Matcha Latte", 3.00),
    Product("Blueberry Muffin", 1.50),
    Product("Croissant", 1.50),
    Product("Water", 2.00),
    Product("Pancakes", 4.00),
    Product("Breakfast sandwich", 2.50)
}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
