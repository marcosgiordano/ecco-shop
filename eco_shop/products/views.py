import contextlib
from contextvars import Context
from multiprocessing import context
from django.shortcuts import render
from products.models import food
from products.models import freshfood
from products.models import drinks

def create_food(request):
    food_product= food.objects.create (name='lata de durazno', price= 350, kilos= 0.500,)
    context = {
        'food_product': food_product
    }
    return render(request, 'food_product.html', context=context)

def create_freshfood(request):
    freshfood_product= freshfood.objects.create (name='manzana', price= 50, kilos= 0.2, rottendays= 10)
    context = {
        'freshfood_product': freshfood_product
    }
    return render(request, 'freshfood_product.html', context=context)

def create_drinks(request):
    drinks_product= drinks.objects.create (name='fanta', price= 250, gallons= 0.2,)
    context = {
        'drinks_product': drinks_product
    }
    return render(request, 'drinks_product.html', context=context)

def list_food(request):
    list_food= food.objects.all()
    context={
        'list_food' : list_food
    }
    return render(request, 'list_food.html', context={})

def list_freshfood(request):
    list_freshfood= freshfood.objects.all()
    context={
        'list_freshfood' : list_freshfood
    }
    return render(request, 'list_freshfood.html', context={})

def list_drinks(request):
    list_drinks= drinks.objects.all()
    context={
        'list_drinks' : list_food
    }
    return render(request, 'list_drinks.html', context={})

