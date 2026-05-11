
from django.shortcuts import render

# Create your views here.
from .models import CoffeeItem, Customer, Order, Event

def order_list(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    product = CoffeeItem.objects.all()
    return render(request, 'cafe/order_list.html', {'orders': orders, 'customers': customers, 'product': product})

def base(request):
    return render(request, 'cafe/base.html')

def home(request):
    return render(request, 'cafe/home.html')

def event(request):
    events = Event.objects.all()
    return render(request, 'cafe/event.html', {'events': events})

def about(request):
    return render(request, 'cafe/about.html')


