from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="home"),
    path('create_saldo', create_saldo, name="create_saldo"),
    path('create_charge', create_charge, name="create_charge"),
    path('create_payment', create_payment, name="create_payment"),
]