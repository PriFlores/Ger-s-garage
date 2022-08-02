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


def product_list(request, categoryId=None):
    category = None
    products = Product.objects.all()
    CountCategories = Category.objects.annotate(numProducts=Count('products'))
    if (categoryId):
        category = get_object_or_404(Category, id=category)
        products.filter(category=category)
    paginator = Paginator(product_list, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products1 = paginator.page(page)
    except (EmptyPage, InvalidPage):
        order = paginator.page(paginator.num_pages)
    return render(request, 'products.html',
                  {'products': products,
                   'countcat': CountCategories})
