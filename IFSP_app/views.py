from django.shortcuts import render, get_object_or_404
from .models import Category, Manufacturer, Tool, ToolCopy
from django.contrib.auth.decorators import login_required, permission_required

def home(request):
    return render(request, 'home.html')

def manufacturers(request):
    manufacturers = Manufacturer.objects.all()
    context = {
        'manufacturers': manufacturers,
    }
    return render(request, 'manufacturers.html', context=context)


def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context=context)


def manufacturer(request, manufacturer_id):
    single_manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
    return render(request, 'manufacturer.html', {'manufacturer': single_manufacturer})


def tools(request):
    tools = Tool.objects.all()
    context = {
        'tools': tools,
    }
    return render(request, 'tools.html', context=context)


def tool(request, tool_id):
    single_tool = get_object_or_404(Tool, pk=tool_id)
    return render(request, 'tool.html', {'tool': single_tool})

@login_required()
def mytools(request):
    toolcopies = ToolCopy.objects.filter(customer=request.user.id)
    toolcopies_all = ToolCopy.objects.all()
    context = {
        'toolcopies': toolcopies,
        'toolcopies_all': toolcopies_all,
    }
    return render(request, 'user_tools.html', context=context)


