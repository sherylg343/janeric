from django.shortcuts import render


def about(request):
    """ A view to render about.html page """
    return render(request, "about/about.html")

