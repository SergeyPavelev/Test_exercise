from django import template
from menu.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu = MenuItem.objects.filter(menu__name=menu_name, parent=None).prefetch_related('children')
    return menu
