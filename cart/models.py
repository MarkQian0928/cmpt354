from django.db import models
from shoes.models import Shoes
from users.models import CustomUser

class Cart(models.Model):
    CartID = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    data_added = models.DateField(auto_now_add = True)
    
    class Meta:
        db_table = 'Cart'
        ordering = ['data_added']

    def __str__(self):
        return self.CartID

class CartItems(models.Model):
    CartID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    quanity = models.IntegerField()
    active = models.BooleanField(default = True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.quanity * self.shoe.price
    
    def __str__(self):
        return self.shoe
