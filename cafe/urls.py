from django.contrib import admin
from django.urls import include, path
from cafe import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('orders/', views.order_list, name='order_list'),
    path('events/', views.event, name='event'),
    path('about/', views.about, name='about'),
]