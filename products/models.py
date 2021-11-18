from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField(max_length=250)
    stock = models.IntegerField()
    image = models.CharField(max_length=2050)


class Offer(models.Model):
    code = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    discount = models.FloatField(max_length=250)




