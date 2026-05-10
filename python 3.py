python 3
import sqlite3

conn = sqlite3.connect('pink_cafe.db')
cursor = conn.cursor()



queries = [
    """
    CREATE TABLE IF NOT EXISTS customers (
    customer_is INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    loyalty_points INTEGER DEFAULT 0
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS menu (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    customer_id INTEGER,
    order_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
    """
]

for query in queries:
    cursor.execute(query)


    cursor.execute("INSERT OR IGNORE INTO menu (name, price, category) VALUES (?, ? , ?)",
                   ('Rose Latte', 5.00, 'Drinks')
                   ('Rose Latte', 5.00, 'Drinks')
                   ('Pink Hibiscus Tea', 4.00, 'Drinks')
                    ('Espresso', 2.50, 'Drinks')
                    ('Pink Rose cupcake', 2.00, 'Sweets')
                    ('Matcha Latte', 3.00, 'Drinks')
                    ('Blueberry Muffin', 1.50, 'Food')
                    ('Crissant', 1.50, 'Food')
                    ('Water', 2.00, 'Drinks')
                    ('Panakes', 4.00, 'Food')
                    ('Breakfast sandwich', 2.50, 'Drinks'))
    





    conn.commit()
    conn.close()

    print("Pink Cafe database and tables created sucessfully!")