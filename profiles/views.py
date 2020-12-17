from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm, USZipCodeField, USStateSelect


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
