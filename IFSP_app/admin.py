from django.contrib import admin
from .models import Category, Manufacturer, Tool, ToolCopy, User

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Tool)
admin.site.register(ToolCopy)


