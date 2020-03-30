from django.shortcuts import render
from websites.models import Website


def do_search(request):
    websites = Website.objects.filter(name__icontains=request.GET['q'])
    return render(request, "websites.html", {"websites": websites})
