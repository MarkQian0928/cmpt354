from django.db import models

class Cart(models.Model):
    CartID = models.AutoField(primary_key=True)
    CustID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.CustID

class cartItems(models.Model):
    ItemID = models.AutoField(primary_key=True)
    CartID = models.ForeignKey(Cart, on_delete=models.CASCADE, default = Cart.CartID)
    ShoeID = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    NumberToBuy = models.IntegerField()
    
    def __str__(self):
        return self.ShoeID
