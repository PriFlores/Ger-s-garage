from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>', views.remove_cart, name='remove_cart'),
    path('empty_cart/', views.empty_cart, name='empty_cart'),

]