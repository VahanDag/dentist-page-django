from django.shortcuts import render

def index(request):
    return render(request,"index.html")


def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "hizmetler.html")

def contact(request):
    return render(request, "contact.html")

def randevu(request):
    return render(request, "randevu.html")