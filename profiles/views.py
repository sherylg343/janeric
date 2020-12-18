from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm, USZipCodeField, USStateSelect

from checkout.models import Order


def profile(request):
    """ Display the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    defaultship_state = USStateSelect()
    defaultship_zipcode = USZipCodeField()
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'defaultship_state': defaultship_state,
        'defaultship_zipcode': defaultship_zipcode,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
