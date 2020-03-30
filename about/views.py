from django.shortcuts import render


# Create your views here.
def about_page(request):
    """A View that renders the about contents page"""
    return render(request, "about.html")
