from django.contrib import admin
from .models import *


@admin.register(Item)
class Items(admin.ModelAdmin):
    list_display = ('name', 'price')