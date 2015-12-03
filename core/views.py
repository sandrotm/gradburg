from django.shortcuts import render
from .models import Flat, FlatType, Image, Page

# not used currently
def home(request):
    context = {}
    return render(request, 'core/pages/home.html', context)

def nadzaladevi(request):
    context = {}
    return render(request, 'core/pages/nadzaladevi.html', context)

# not used currently
def aboutUs(request):
    context = {}
    context['images'] = Image.objects.filter(title__contains='ძველი')
    return render(request, 'core/pages/aboutUs.html', context)

def process(request):
    context = {}
    context['images'] = Image.objects.filter(title__contains='პროცესი').order_by("date_taken")
    return render(request, 'core/pages/process.html', context)

def flats(request):
    context = {}
    context['flats'] = Flat.objects.all()
    context['flat_group1'] = Flat.objects.filter(type__title='48მ2 ბინა').order_by('-floor')
    context['flat_group2'] = Flat.objects.filter(type__title='73მ2 ბინა').order_by('-floor')
    context['flat_group3'] = Flat.objects.filter(type__title='110.5მ2 ბინა').order_by('-floor')
    context['flat_groups'] = zip(context['flat_group1'], context['flat_group2'], context['flat_group3'])
    context['flat_types'] = FlatType.objects.all()
    context['highlights'] = ['unnamed_5.png', 'unnamed_4.png', 'unnamed_6.png']
    context['flat_types_zip'] = zip(context['flat_types'], context['highlights'])
    context['floors'] = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
    return render(request, 'core/pages/flats.html', context)

def contact(request):
    context = {}
    return render(request, 'core/pages/contact.html', context)