from django.db import models

class Item(models.Model):
    cur = (
    ('rub', 'rub'),
    ('usd', 'usd'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=5, choices=cur, default='₽')

    def __str__(self):
        return self.name
    
class Discount(models.Model):
    code = models.CharField(max_length=30)
    discount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.code
    
class Tax(models.Model):
    name = models.CharField(max_length=100)
    tax = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey('Tax', on_delete=models.SET_NULL, null=True, blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        total_price = 0
        for item in self.items.all():
            total_price += item.price
        self.total =  total_price
        super(Order, self).save(*args, **kwargs)
