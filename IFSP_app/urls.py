from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name="home"),
   path('manufacturers/', views.manufacturers, name="manufacturers"),
   path('manufacturers/<int:manufacturer_id>', views.manufacturer, name='manufacturer'),
   path('categories/', views.categories, name="categories"),
   path('tools/', views.tools, name="tools"),
   path('tools/<int:tool_id>', views.tool, name='tool'),
   path('mytools/', views.mytools, name='user-tools'),
]

