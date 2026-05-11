
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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

def new_order(request):
    if not request.user.is_authenticated:
        return render(request, 'cafe/new_order.html', {'error': 'You must be logged in to place an order.'})
    coffees = CoffeeItem.objects.all()
    if request.method == 'POST':
        selected_coffees = request.POST.getlist('coffees')
        if selected_coffees:
            customer, created = Customer.objects.get_or_create(
                name=request.user.username,
                defaults={'email': request.user.email or ''}
            )
            order = Order.objects.create(customer=customer)
            order.items.set(selected_coffees)
            return redirect('order_list')
    return render(request, 'cafe/new_order.html', {'coffees': coffees})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'cafe/login.html', {'login_error': 'Invalid credentials'})
    return render(request, 'cafe/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'cafe/login.html', {'register_error': 'Username already exists'})
        else:
            return render(request, 'cafe/login.html', {'register_error': 'Passwords do not match'})
    return render(request, 'cafe/login.html')

def login(request, user=None):
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth import login as auth_login

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'cafe/login.html', {'form': form})

def logout(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return redirect('home')

