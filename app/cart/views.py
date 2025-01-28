from django.shortcuts import render, redirect
from shop.models import Product
from cart.cart import Cart

def add_to_cart(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)
    return redirect('cart:cart')  # Добавлен namespace для маршрута корзины

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart:cart')

def get_cart(request):
    return render(request, 'cart.html', {'cart': Cart(request)})