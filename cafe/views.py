from django.shortcuts import render

# Create your views here.
from .models import CreateOrder

def order_list(request):
    orders = CreateOrder.objects.all()
    return render(request, 'cafe/order_list.html', {'orders': orders})



