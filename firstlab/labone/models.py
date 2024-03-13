from django.db import models
from django.db.models import DecimalField


class Saldo(models.Model):
    apartment = models.IntegerField(primary_key=True, unique=True)
    insaldo = DecimalField(max_digits=8, decimal_places=2)
    outsaldo = DecimalField(max_digits=8, decimal_places=2)
    january = DecimalField(max_digits=8, decimal_places=2)
    february = DecimalField(max_digits=8, decimal_places=2)
    march = DecimalField(max_digits=8, decimal_places=2)
    april = DecimalField(max_digits=8, decimal_places=2)
    may = DecimalField(max_digits=8, decimal_places=2)
    june = DecimalField(max_digits=8, decimal_places=2)
    july = DecimalField(max_digits=8, decimal_places=2)
    august = DecimalField(max_digits=8, decimal_places=2)
    september = DecimalField(max_digits=8, decimal_places=2)
    october = DecimalField(max_digits=8, decimal_places=2)
    november = DecimalField(max_digits=8, decimal_places=2)
    december = DecimalField(max_digits=8, decimal_places=2)


class Charge(models.Model):
    apartment = models.IntegerField(primary_key=True, unique=True)
    january = DecimalField(max_digits=8, decimal_places=2)
    february = DecimalField(max_digits=8, decimal_places=2)
    march = DecimalField(max_digits=8, decimal_places=2)
    april = DecimalField(max_digits=8, decimal_places=2)
    may = DecimalField(max_digits=8, decimal_places=2)
    june = DecimalField(max_digits=8, decimal_places=2)
    july = DecimalField(max_digits=8, decimal_places=2)
    august = DecimalField(max_digits=8, decimal_places=2)
    september = DecimalField(max_digits=8, decimal_places=2)
    october = DecimalField(max_digits=8, decimal_places=2)
    november = DecimalField(max_digits=8, decimal_places=2)
    december = DecimalField(max_digits=8, decimal_places=2)


class Payment(models.Model):
    apartment = models.IntegerField(primary_key=True, unique=True)
    january = DecimalField(max_digits=8, decimal_places=2)
    february = DecimalField(max_digits=8, decimal_places=2)
    march = DecimalField(max_digits=8, decimal_places=2)
    april = DecimalField(max_digits=8, decimal_places=2)
    may = DecimalField(max_digits=8, decimal_places=2)
    june = DecimalField(max_digits=8, decimal_places=2)
    july = DecimalField(max_digits=8, decimal_places=2)
    august = DecimalField(max_digits=8, decimal_places=2)
    september = DecimalField(max_digits=8, decimal_places=2)
    october = DecimalField(max_digits=8, decimal_places=2)
    november = DecimalField(max_digits=8, decimal_places=2)
    december = DecimalField(max_digits=8, decimal_places=2)
