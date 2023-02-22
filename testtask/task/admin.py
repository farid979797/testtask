from django.contrib import admin
from .models import *

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_id', 'menu_id')


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
