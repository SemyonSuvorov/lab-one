from django.shortcuts import render, redirect
from .forms import *

def index(request):
    saldo = Saldo.objects.all()
    charges = Charge.objects.all()
    payments = Payment.objects.all()
    saldo_one = Saldo.objects.get(apartment=1)
    charges_one = Charge.objects.get(apartment=1)
    payments_one = Payment.objects.get(apartment=1)
    count_charges = 0
    count_payments = 0
    for field in Charge._meta.get_fields():
        value_charge = getattr(charges_one, field.name)
        value_payment = getattr(payments_one, field.name)
        count_charges += value_charge
        count_payments += value_payment
    result_payment = saldo_one.insaldo + (count_charges - count_payments)
    return render(request, 'labone/index.html',
                  {'saldo': saldo, 'charges': charges, 'payments': payments,
                   'saldo_one': saldo_one, 'charges_one': charges_one, 'payments_one': payments_one,
                   'count_charges': count_charges, 'count_payments': count_payments,
                   'result_payment': result_payment})


def create_saldo(request):
    if request.method == 'POST':
        form = AddSaldoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(create_charge)
            except:
                form.add_error(None, "Ошибка")
    else:
        form = AddSaldoForm()

    return render(request, 'labone/create_saldo.html', {'form': form})


def create_charge(request):
    if request.method == 'POST':
        form = AddChargeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(create_payment)
            except:
                form.add_error(None, "Ошибка")
    else:
        form = AddChargeForm()
    return render(request, 'labone/create_charge.html', {'form': form})


def create_payment(request):
    if request.method == 'POST':
        form = AddPaymentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                form.add_error(None, "Ошибка")
    else:
        form = AddPaymentForm()
    return render(request, 'labone/create_payment.html', {'form': form})
