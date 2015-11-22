from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'core/pages/home.html', context)

def nadzaladevi(request):
    context = {}
    return render(request, 'core/pages/nadzaladevi.html', context)

def aboutUs(request):
    context = {}
    return render(request, 'core/pages/aboutUs.html', context)

def contact(request):
    context = {}
    return render(request, 'core/pages/contact.html', context)