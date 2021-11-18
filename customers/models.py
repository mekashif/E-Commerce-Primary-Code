from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=250)
    age = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

