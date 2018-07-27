from django.db import models
from users.models import CustomUser
from shoes.models import Shoes
from datetime import date

class transactionHistory(models.Model):
    numPurchased = models.IntegerField(blank=True)
    shoeName = models.CharField(max_length=100, default='', blank=True)
    customerName = models.CharField(max_length=100, default='', blank=True)
    price = models.IntegerField(default=0, blank = True)
    time = models.DateField(auto_now_add=True)