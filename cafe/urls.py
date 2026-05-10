from django.contrib import admin
from django.urls import include, path

from cafe import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('base/', views.base, name='base'),
]