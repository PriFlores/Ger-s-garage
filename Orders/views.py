from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Orders, OrdersItem
from Products.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from shop_cart.models import Cart,CartItem
from shop_cart.views import _cart_id
from .Invoice import html_to_pdf
import stripe

@login_required()
def orders_create(request, total=0, cart_items = None):
    if request.method == 'POST':
        cart = Cart.objects.get(cart_id= _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            total += (item.quantity * item.product.price)
            print('Total',total)
            charge = stripe.Charge.create(
                amount=str(int(total*100)),
                currency= 'EUR',
                description='Credit card charge',
                source=request.POST['stripeToken']
            )
        if request.user.is_authenticated:
            email = str(request.user.email)
            order_details = Orders.objects.create(emailAddress = email)
            order_details.save()
        try:
            cart = Cart.objects.get(cart_id =_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart)
            for order_item in cart_items:
                oi = OrdersItem.objects.create(
                    product = order_item.product.name,
                    quantity = order_item.quantity,
                    price = order_item.product.price,
                    orders = order_details)
                total = (order_item.quantity * order_item.product.price)
                oi.save()
                products = Product.objects.get(id=order_item.product.id)
                if products.stock > 0:
                    products.stock = int(order_item.product.stock - order_item.quantity)
                    products.save()
                    order_item.delete()
        except ObjectDoesNotExist:
            pass
        return render(request, 'order.html', dict(cart_items = cart_items, total=total))

@login_required()
def orders_history(request):
    email = str(request.user.email)
    order_details = Orders.objects.filter(emailAddress=email)
    paginator = Paginator(order_details, 20)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page=1
    try:
        orders = paginator.page(page)
    except (EmptyPage, InvalidPage):
        orders = paginator.page(paginator.num_pages)
    return render(request, 'order_list.html',{'order_details':order_details})



def orders_invoice(request ,order_id):
    # getting the template
    order_details = Orders.objects.get(id=order_id)
    pdf = html_to_pdf('orderInvoice.html',{'order_details':order_details})
    #return render(request,'orderInvoice.html',{'order_details':order_details})
    # rendering the template
    return HttpResponse(pdf, content_type='application/pdf')