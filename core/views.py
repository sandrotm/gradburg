from django.shortcuts import render
from .models import Flat, FlatType, Image, Page

def home(request):
    context = {}
    return render(request, 'core/pages/home.html', context)

def nadzaladevi(request):
    context = {}
    context['flats'] = Flat.objects.all()
    context['flat_group1'] = Flat.objects.filter(type__title='მცირე ბინა').order_by('-floor')
    #context['flat_group1'] = Flat.objects.filter(floor=3).order_by('-floor')
    context['flat_group2'] = Flat.objects.filter(type__title='საშუალო ბინა').order_by('-floor')
    context['flat_group3'] = Flat.objects.filter(type__title='დიდი ბინა').order_by('-floor')
    context['flat_types'] = FlatType.objects.all()
    context['floors'] = list(range(8, 0, -1))
    return render(request, 'core/pages/nadzaladevi.html', context)

def aboutUs(request):
    context = {}
    context['images'] = Image.objects.all()
    return render(request, 'core/pages/aboutUs.html', context)

def contact(request):
    context = {}
    return render(request, 'core/pages/contact.html', context)