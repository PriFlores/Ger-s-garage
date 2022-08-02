from django.db import models
import Products


class Category(models.Model):
    name = models.TextField(max_length=25, default='')
    products = models.ManyToManyField('Product')

    def get_products(self):
        return Products.objects.filter(category=self)

    def __str__(self):
        return self.name


### I tried to creat a subcategory but it was too complex and to save effort I just left it as it is
# class Subcategory(models.Model):
#   name = models.TextField(max_length=25, default='')
#  category = models.ManyToManyField('Category')

# def get_category(self):
#    return Subcategory.objects.filter(category=self)

class Product(models.Model):
    # productID = models.TextField(max_length=10) The ID is already generated automatically by SQLite
    name = models.TextField(max_length=25, default='')
    description = models.TextField(max_length=100, default='')
    brand = models.TextField(max_length=25, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='images/', blank=True)
    stock = models.IntegerField()
    def __str__(self):
        return self.name
