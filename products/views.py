from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def index(requests):
    products= Product.objects.all()
    return render(requests,'index.html',
                {'products':products}  )


def new(requests):
    return HttpResponse('New Products')


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)  # ✅ FIXED
    cart[product_id_str] = cart.get(product_id_str, 0) + 1
    request.session['cart'] = cart
    return redirect('index')


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id_str, quantity in cart.items():
        product_id = int(product_id_str)  # ✅ FIXED
        product = get_object_or_404(Product, pk=product_id)
        subtotal = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        total += subtotal

    return render(request, 'products/cart.html', {
        'cart_items': cart_items,
        'total': total
    })



def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('view_cart')


def update_cart(request):
    product_id = request.POST.get('product_id')
    quantity = request.POST.get('quantity')

    cart = request.session.get('cart', {})
    if product_id and quantity:
        try:
            quantity = int(quantity)
            if quantity > 0:
                cart[product_id] = quantity
            else:
                del cart[product_id]
        except ValueError:
            pass

    request.session['cart'] = cart
    return redirect('view_cart')