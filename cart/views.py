from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request):
    """ Add a quantity of the specified product to the shopping cart """

    product_id = request.POST.get('selected_product_id')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')
    else:
        cart[product_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[product_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')
    else:
        cart.pop(product_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=product_id)
        cart = request.session.get('cart', {})

        cart.pop(product_id)
        messages.success(request, f'Removed {product.name} from your cart')
 
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
