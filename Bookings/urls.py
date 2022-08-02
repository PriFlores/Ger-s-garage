from django.urls import path

from . import views

urlpatterns = [
    path('', views.new_appointment, name='Bookings'),
    path('history/', views.bookings_history, name= 'bookings_history'),
]