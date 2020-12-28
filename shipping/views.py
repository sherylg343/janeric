from django.shortcuts import render


def shipping(request):
    """ A view to render shipping.html page """
    return render(request, 'shipping/shipping.html')

