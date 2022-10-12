from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name="home"),
   path('manufacturers/', views.manufacturers, name="manufacturers"),
   path('manufacturers/<int:manufacturer_id>', views.manufacturer, name='manufacturer'),
]