from django.shortcuts import render
from . import models

def index(request):
    menus = models.Menu.objects.filter(menu_location_url=request.get_full_path())
    
    data = {
        'title': 'Home',
        'menus': menus,
    }
    
    return render(request, 'menu/index.html', context=data)

def show_menu(request, name_menu):
    menu = models.Menu.objects.get(named_url=name_menu)
    other_menus = models.Menu.objects.filter(menu_location_url=request.get_full_path())
    
    data = {
        'title': f'{name_menu}',
        'name_menu': menu,
        'other_menus': other_menus,
    }
    
    return render(request, 'menu/page_menu.html', context=data)

def show_category(request, name_menu, name_category):
    menu = models.Menu.objects.get(named_url=name_menu)
    category = models.MenuItem.objects.get(named_url=name_category)
    other_menus = models.Menu.objects.filter(menu_location_url=request.get_full_path())
    
    data = {
        'title': f'{name_category}',
        'name_menu': menu,
        'category': category,
        'other_menus': other_menus,
    }
    
    return render(request, 'menu/page_category.html', context=data)

def show_subcategory(request, name_menu, name_category, name_subcategory):
    subcategory = models.MenuItem.objects.get(named_url=name_subcategory)
    other_menus = models.Menu.objects.filter(menu_location_url=request.get_full_path())
    
    data = {
        'title': f'{subcategory}',
        'subcategory': subcategory,
        'other_menus': other_menus,
    }
    
    return render(request, 'menu/page_subcategory.html', context=data)
