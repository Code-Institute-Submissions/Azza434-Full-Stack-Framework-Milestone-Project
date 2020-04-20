from django.shortcuts import render
from .models import Website


def all_websites(request):
    """
    A view created to render website.html
    """
    websites = Website.objects.all()
    return render(request, "websites.html", {"websites": websites})
