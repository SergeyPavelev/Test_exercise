from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    url = models.CharField(
        max_length=255,
        blank=True,
    )
    named_url = models.CharField(
        max_length=255,
        blank=True,
    )
    
    menu_location_url = models.CharField(
        max_length=255,
        blank=True,
        default='/',
    )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            return reverse(self.named_url)
    
    def get_location_menu_url(self):
        return self.menu_location_url

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
    )
    url = models.CharField(
        max_length=255,
        blank=True,
    )
    named_url = models.CharField(
        max_length=255,
        blank=True,
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            return reverse(self.named_url)
    
    def get_item_index(self):
        items = list(MenuItem.objects.all())
        return items.index(self)
    
    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'
    
