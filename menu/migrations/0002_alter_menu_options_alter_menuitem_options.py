# Generated by Django 5.0.4 on 2024-04-11 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menus'},
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'verbose_name': 'Menu Itmem', 'verbose_name_plural': 'Menu Itmems'},
        ),
    ]
