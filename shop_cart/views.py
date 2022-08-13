from django.shortcuts import render, redirect, get_object_or_404
from Products.models import Product
from .models import Cart, CartItem
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import stripe

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart (request, product_id):#add items to the cart/if there is no cart it creates one
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart= Cart.objects.create(cart_id = _cart_id(request))
        cart.save()
    try:
        cart_item= CartItem.objects.get(product= product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.add_message(request, messages.INFO, 'Sorry this item is no longer available')
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart_detail')

def cart_detail(request, total= 0 , counter = 0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    key = settings.STRIPE_PUBLISHABLE_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY#loads in the created stripe keys to create the stripe session
    desc = 'new order'
    stotal = int(total*100)
    return render(request, 'shop_cart.html', dict(cart_items= cart_items, total = total, counter= counter, key=key, stotal=stotal, desc=desc ))

def remove_cart(request, product_id):#removes one item from the cart
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item= CartItem.objects.get(product=product, cart= cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')


def empty_cart(request):#empties th entire cart
    cart= Cart.objects.get(cart_id= _cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart)
    for cart_item in cart_items:
        cart_items.delete()
    return redirect('cart_detail')