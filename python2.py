python2
import tkinter as tk
from tkinter import messagebox
from logic import menu, Order

class PinkRoseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pink Rose Cafe System")
        self.root.geometry("400x500")
        self.root.configure(bg="#ffe4e1")

        self.order = Order()

        tk.label(root, text="Pink Rose Cafe")