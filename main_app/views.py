from django.shortcuts import render, redirect
from main_app.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    print(session.id)
    return JsonResponse({'id': session.id})

def item(request, id):
    item = Item.objects.get(id = id)
    context = {
            'item': item,
            'key': settings.STRIPE_PUBLIC_KEY
            }
    return render(request, 'main_app/item.html', context)



def create_payment_intent(amount, payment_method_id):
    print(payment_method_id)
    intent = stripe.PaymentIntent.create(
        amount=int(amount * 100),
        currency='usd',
        payment_method=payment_method_id,
        payment_method_types=['card'],
        payment_method_options={
            'card': {
                'request_three_d_secure': 'any'
            }
        },
        metadata={
            'integration_check': 'accept_a_payment'
        },
        confirm=True
    )
    return intent.client_secret


@csrf_exempt
def payment_intent(request):
    if request.method == 'GET':
        return render(request, 'main_app/chekout.html')
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        payment_method = int(request.POST['payment_method_id'])
        client_secret = create_payment_intent(amount, payment_method)
        return JsonResponse({'client_secret': client_secret})



def order(request):
    item = Item.objects.all()

    context = {
            'item': item,
            'key': settings.STRIPE_PUBLIC_KEY
            }
    return render(request, 'main_app/orders.html', context)