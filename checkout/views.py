from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import USZipCodeField, USStateSelect, OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    state = USStateSelect()
    zipcode = USZipCodeField()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'state': state,
        'zipcode': zipcode,
    }

    return render(request, template, context)
