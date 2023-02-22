from django.db import models

class Item(models.Model):
    cur = (
    ('rub', '₽'),
    ('usd', '$'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=5, choices=cur, default='₽')

class Discount(models.Model):
    code = models.CharField(max_length=30)
    discount = models.DecimalField(max_digits=6, decimal_places=2)

class Tax(models.Model):
    name = models.CharField(max_length=100)
    tax = models.DecimalField(max_digits=6, decimal_places=2)

class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey('Tax', on_delete=models.SET_NULL, null=True, blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
