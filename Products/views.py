from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category, Product
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, InvalidPage


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'all_products_list'

    def categories(self):
        return Category.objects.all()

def ListByCat(request,id):#when a category is selected the product fields are filtered to only allow the products of the selected category are shown
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category_id = category.id)
    return render(request, 'categories.html', {'Category': category,'products':products})

def product_list(request, categoryId=None):#list all of the products available for the user to purchase
    category = None
    products = Product.objects.all()
    if (categoryId):
        category = get_object_or_404(Category, id=category)
        products.filter(category=category)
    paginator = Paginator(product_list, 1)
    try:
        page = int(request.GET.get('page', '1'))#if there is more than one page available then this allows the user to scroll through them
    except:
        page = 1
    try:
        products1 = paginator.page(page)
    except (EmptyPage, InvalidPage):
        order = paginator.page(paginator.num_pages)
    return render(request, 'products.html',
                  {'products': products})