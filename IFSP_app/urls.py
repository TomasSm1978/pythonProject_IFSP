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
   path('accounts/sign_up/', views.sign_up, name='sign_up'),
   path('accounts/user_profile/', views.user_profile, name='user_profile'),
   path('toolcopy/new/', views.ToolCopyCreateView.as_view(), name='toolcopy-create'),
   path('toolcopy/<str:pk>/update', views.ToolCopyUpdateView.as_view(), name='toolcopy-update'),
   path('toolcopy/<str:pk>/reserve', views.ToolCopyUpdateView_reserve.as_view(), name='toolcopy-update-reserve'),
   path('toolcopy/<str:pk>/cancel_reserve', views.ToolCopyUpdateView_cancel_reserve.as_view(), name='toolcopy-update-cancel-reserve'),
   path('toolcopy/<str:pk>/delete', views.ToolCopyDeleteView.as_view(), name='toolcopy-delete'),

]

