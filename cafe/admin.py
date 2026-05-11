from django.contrib import admin
from .models import CoffeeItem, Customer, Event, Order

admin.site.register(CoffeeItem)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Event)
