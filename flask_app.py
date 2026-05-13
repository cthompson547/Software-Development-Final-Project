import sqlite3
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# File path setup for PythonAnywhere
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "cafe.db")


class CafeMenu:
    def __init__(self):
        self.items = [
            {"name": "Rose Latte", "price": 5.00, "icon": "☕", "mood": "Anxious"},
            {"name": "Pink Hibiscus Tea", "price": 4.00, "icon": "🌺", "mood": "Stressed"},
            {"name": "Pink Rose Cupcake", "price": 2.00, "icon": "🧁", "mood": "Sad"},
            {"name": "Matcha Latte", "price": 3.00, "icon": "🍵", "mood": "Tired"},
            {"name": "Breakfast Sandwich", "price": 2.50, "icon": "🥪", "mood": "Hungry"}
        ]
    def get_all(self):
        return self.items


class JournalManager:
    def __init__(self):
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS gratitude_notes
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           note TEXT NOT NULL,
                           created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()

    def save_note(self, content):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO gratitude_notes (note) VALUES (?)", (content,))
        conn.commit()
        conn.close()

    def get_recent(self):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT note, strftime('%m/%d %H:%M', created_at) FROM gratitude_notes ORDER BY created_at DESC LIMIT 3")
        notes = cursor.fetchall()
        conn.close()
        return notes


class CafeSystem:
    def __init__(self):
        self.menu = CafeMenu()
        self.journal = JournalManager()


cafe_system = CafeSystem()


@app.route('/')
def home():
    menu = cafe_system.menu.get_all()
    notes = cafe_system.journal.get_recent()
    return render_template('index.html', menu=menu, notes=notes)

@app.route('/save_note', methods=['POST'])
def save_note():
    user_note = request.form.get('note')
    if user_note:
        cafe_system.journal.save_note(user_note)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
