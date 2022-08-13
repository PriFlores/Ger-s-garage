from django.contrib import admin

from .models import Product
from .models import Category
#this file allows the administrator to control the models tethered

admin.site.register(Product)
admin.site.register(Category)





