from django.shortcuts import render, get_object_or_404
from .models import Category, Manufacturer, Tool, ToolCopy

def home(request):
    return render(request, 'home.html')

def manufacturers(request):
    manufacturers = Manufacturer.objects.all()
    toolcopy = ToolCopy.objects.all()
    context = {
        'manufacturers': manufacturers,
        'toolcopy': toolcopy
    }
    return render(request, 'manufacturers.html', context=context)


def manufacturer(request, manufacturer_id):
    single_manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
    return render(request, 'manufacturer.html', {'manufacturer': single_manufacturer})