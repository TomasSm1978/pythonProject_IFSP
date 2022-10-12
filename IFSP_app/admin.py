from django.contrib import admin
from .models import Category, Manufacturer, Tool, ToolCopy


admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Tool)
admin.site.register(ToolCopy)


