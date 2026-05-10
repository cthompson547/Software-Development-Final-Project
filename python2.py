python5
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

        tk.Label(root, text="Pink Rose Cafe", font=("Courier", 24, "bold"),
                 bg="#ffe4e1", fg="d02090").pack(pady=20)
        

        tk.Label(root, text="Select Items:",bg="#ffe4e1").pack()
        for product in menu:
           btn = tk.Button(root, text=f"{product.name} - ${product.price:.2f}",
                           width=30, command=lambda p=product: self.add_to_order(p))
           btn.pack(pady=5)


        self.total_label = tk.label = tk.Label(root, text="Total: $0.00", font=("Arial", 14),
                                               bg="#ffe4e1", fg="black")
        self.total_label.pack(pady=20)


        tk.Button(root, text="Complete Order", bg="#ff69b4", fg="white",
                  command=self.checkout).pack(pady=10)
        

        def add_to_order(self, product): 
            self.order.add_item(product)
            self.total_label.config(text="Total: ${self.order.calculate_total():.2f}")

        def checkout(self):
            total = self.order.calculate_total()
            if total > 0:
                messagebox.showinfo("Receipt", f"Thank your for visiting Pink Rose Cafe!\nTotal: ${total:.2f}")
                self.order.reset()
                self.total_label.config(text="Total: $0.00")
            else:
                messagebox.showwarning("Error", "Order is empty!")

    if __name__ == "__main__":
        root = tk.Tk()
        app = PinkRoseApp(root)
        root.mainloop()
        


