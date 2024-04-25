from django.urls import path
from . import views


app_name = 'menu'

urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:name_menu>/', views.show_menu, name='page_menu'),
    path('<slug:name_menu>/<slug:name_category>/', views.show_category, name='page_category'),
    path('<slug:name_menu>/<slug:name_category>/<slug:name_subcategory>/', views.show_subcategory, name='page_subcategory'),
]
