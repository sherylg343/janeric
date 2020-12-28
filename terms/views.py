from django.shortcuts import render


def terms(request):
    """ A view to render terms.html page """
    return render(request, 'terms/terms.html')
