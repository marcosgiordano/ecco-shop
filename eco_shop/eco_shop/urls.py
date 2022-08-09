
from django.contrib import admin
from django.urls import path
from products.views import create_food
from products.views import create_freshfood
from products.views import create_drinks
from products.views import list_drinks
from products.views import list_food
from products.views import list_freshfood
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_food/', create_food, name='create_food'),
    path('create_freshfood/', create_freshfood, name='create_freshfood'),
    path('create_drinks/', create_drinks, name='create_drinks'),
    path('list_drinks/', list_drinks, name='list_drinks'),
    path('list_food/', list_food, name='list_food'),
    path('list_freshfood/', list_freshfood, name='list_freshfood'),

]
