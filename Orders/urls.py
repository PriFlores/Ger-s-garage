from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.orders_create, name= 'orders_create'),
    path('history/', views.orders_history, name= 'orders_history'),
    path('history/<int:order_id>', views.orders_invoice,name ='orders_invoice')
]