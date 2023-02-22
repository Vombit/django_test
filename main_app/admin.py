from django.contrib import admin
from .models import *


@admin.register(Item)
class Items(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Discount)
class Discounts(admin.ModelAdmin):
    list_display = ('code',)

@admin.register(Tax)
class Taxs(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Order)
class Orders(admin.ModelAdmin):
    list_display = ('total',)