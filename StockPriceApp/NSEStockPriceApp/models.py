from fileinput import close
from operator import mod
from subprocess import HIGH_PRIORITY_CLASS
from time import time
from unicodedata import name
from django.db import models

# Create your models here.
# for Series


class Series(models.Model):
    series = models.CharField(max_length=100)

#  for Details of Company.


class Company(models.Model):
    symbol = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    isinnumber = models.CharField(max_length=500)

# for securities


class Securities(models.Model):
    date = models.CharField(max_length=100)
    paidup = models.FloatField()
    marketlot = models.IntegerField()
    facevalue = models.FloatField()
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

# for bhavcopy


class Bhavcopy(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    last = models.FloatField()
    previousclose = models.FloatField()
    totaltrdq = models.FloatField()
    totaltrdv = models.FloatField()
    time = models.CharField(max_length=100)
    trades = models.IntegerField()
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
