from django.db import models
from users.models import Retailer
from django.db.models.signals import post_save

class Shoes(models.Model):
    brand = models.CharField(max_length=50, blank=True, default ='')
    category = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank=True)
    description  = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(blank=True)
    numOfAvail = models.IntegerField(default =0, blank=True)
    retailID = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.brand
    