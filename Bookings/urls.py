from django.urls import path

from . import views

urlpatterns = [
    path('', views.new_appointment, name='Bookings'),
    path('payment/', views.bkPay, name='Pay_BK'),
    path('history/', views.bookings_history, name= 'bookings_history'),
]