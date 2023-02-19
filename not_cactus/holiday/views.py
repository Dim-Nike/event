from django.shortcuts import render
from .models import *


def show_landing(req):
    data = {
        'categories': CategoriesHoliday.objects.order_by('name'),
        'events': Event.objects.order_by('name')
    }

    return render(req, 'holiday/landing.html', data)


def show_list_events(req, pk):
    data = {
        'categories': CategoriesHoliday.objects.filter(id=pk),
        'events': Event.objects.order_by('name')
    }

    return render(req, 'holiday/list_products.html', data)

def show_event(req, pk):
    data = {
        'events': Event.objects.filter(id=pk),
        'events_popular': Event.objects.order_by('name')
    }

    return render(req, 'holiday/products.html', data)