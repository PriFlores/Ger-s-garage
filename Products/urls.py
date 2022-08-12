from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path ('',ProductListView.as_view(), name = 'products'),
    path ('categories/<int:id>',views.ListByCat, name = 'category'),
]