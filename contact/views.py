from django.shortcuts import render


# Create your views here.
def contact_page(request):
    """A View that renders the contact contents page"""
    return render(request, "contact.html")
