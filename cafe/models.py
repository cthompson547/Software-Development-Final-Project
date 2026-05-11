from django.db import models

# Class 1: Represents the coffee products
class CoffeeItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default="Pink Rose Themed")

    def __str__(self):
        return self.name

# Class 2: Represents the customers
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

# Class 3: Represents the order system
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # This ManyToManyField is a collection (a list of items)
    items = models.ManyToManyField(CoffeeItem)
    order_date = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        # This logic utilizes a list collection to calculate the price
        prices_list = [item.price for item in self.items.all()]
        return sum(prices_list)

    def __str__(self):
        return f"Order {self.id} for {self.customer.name}"
    
# Class 4: Schedules for events
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name


from django.contrib import admin
from .models import CoffeeItem, Customer, Order
