from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    def __str__(self):
        return self.email

class Customer(models.Model):
    CustID = models.IntegerField(primary_key=True)
    EmailAddress = models.CharField(max_length=40)
    Name = models.CharField(max_length=40)
    DeliveryAddress = models.CharField(max_length=100)
    Password = models.CharField(max_length=40)
    def __str__(self):
        return self.field_name

class Retailer(models.Model):
    RetialID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=40)
    Password = models.CharField(max_length=40)
    def __str__(self):
        return self.field_name
    
class Shoes_owns(models.Model):
    ShoeID = models.IntegerField(primary_key=True)
    Brand = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)
    Size = models.DecimalField()
    Gender = models.CharField(max_length=20)
    Colour = models.CharField(max_length=20)
    Description = models.CharField(max_length=400)
    Price = models.DecimalField()
    NumOfAvail = models.IntegerField()
    RetailID = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    def __str__(self):
        return self.field_name
    
class Transaction_History_belongs(models.Model):
    id = models.AutoField(primary_key=True)
    Sold_Time = model.DateField(auto_now_add=True)
    ShoeID = model.ForeignKey(Shoe_owns)
    CustID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Num_Purchased = models.IntegerField()
    Price = models.DecimalField()
    def __str__(self):
        return self.field_name
    
class CartItems(models.Model):
    id = models.AutoField(primary_key=True)
    CartID = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, default = ShoppingCart.id)
    ShoeID = models.ForeignKey(Shoe_owns, on_delete=models.CASCADE)
    NumberToBuy = models.IntegerField()
    def __str__(self):
        return self.field_name

class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    CustID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return self.field_name


#class PastMonthsHistory(models.Model):
#    id = models.AutoField(primary_key=True)
#    ThisMonth_SoldTime = model.DateField(auto_now_add=True)
#    ThisMonth_CustID = 

    
    
