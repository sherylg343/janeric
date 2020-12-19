from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import USZipCodeField, USStateSelect, OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        print(pid)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
        print(HttpResponse)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)
        print(HttpResponse)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'ship_full_name': request.POST['ship_full_name'],
            'email': request.POST['email'],
            'ship_comp_name': request.POST['ship_comp_name'],
            'ship_phone_number': request.POST['ship_phone_number'],
            'ship_street_address1': request.POST['ship_street_address1'],
            'ship_street_address2': request.POST['ship_street_address2'],
            'ship_city': request.POST['ship_city'],
            'ship_state': request.POST['ship_state'],
            'ship_zipcode': request.POST['ship_zipcode'],
            'bill_full_name': request.POST['bill_full_name'],
            'bill_phone_number': request.POST['bill_phone_number'],
            'bill_street_address1': request.POST['bill_street_address1'],
            'bill_street_address2': request.POST['bill_street_address2'],
            'bill_city': request.POST['bill_city'],
            'bill_state': request.POST['bill_state'],
            'bill_zipcode': request.POST['bill_zipcode'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            print(pid)
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for product_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=product_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. \
                        Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    # Attempt to prefill the form with any info
    # the user maintains in their profile
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'ship_full_name': profile.defaultship_full_name,
                'email': profile.user.email,
                'ship_street_address1': profile.defaultship_street_address1,
                'ship_street_address2': profile.defaultship_street_address2,
                'ship_city': profile.defaultship_city,
                'ship_state': profile.defaultship_state,
                'ship_zipcode': profile.defaultship_zipcode,
                'ship_phone_number': profile.defaultship_phone_number,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    ship_state = USStateSelect()
    bill_state = USStateSelect()
    ship_zipcode = USZipCodeField()
    bill_zipcode = USZipCodeField()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'ship_state': ship_state,
        'bill_state': bill_state,
        'ship_zipcode': ship_zipcode,
        'bill_zipcode': bill_zipcode,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile.defaultship_full_name = order.ship_full_name
            profile.defaultship_comp_name = order.ship_comp_name
            profile.defaultship_street_address1 = order.ship_street_address1
            profile.defaultship_street_address2 = order.ship_street_address2
            profile.defaultship_city = order.ship_city
            profile.defaultship_state = order.ship_state
            profile.defaultship_zipcode = order.ship_zipcode
            profile.defaultship_phone_number = order.ship_phone_number
            profile.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
