from django import forms
from .models import *


class AddSaldoForm(forms.ModelForm):
    class Meta:
        model = Saldo
        fields = "__all__"


class AddPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"


class AddChargeForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = "__all__"
