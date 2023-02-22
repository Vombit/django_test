from django.shortcuts import render, redirect
from main_app.models import *
from django.http import JsonResponse
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def buy(request, id):
    item = Item.objects.get(id = id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price*100),
            },
            'quantity': 1,
        }],
        mode= 'payment',
        success_url = 'http://localhost:8000/success/',
        cancel_url = 'http://localhost:8000/cancel/',
    )
    return JsonResponse({'id': session.id})

def item(request, id):
    item = Item.objects.get(id = id)
    context = {
            'item': item,
            'key': settings.STRIPE_PUBLIC_KEY
            }
    return render(request, 'main_app/item.html', context)


def order(request, id):
    pass