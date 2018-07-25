from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, default='')
    street = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    def __str__(self):
        return self.email






# class UpdateInfo(models.Model):
#     user = models.OneToOneField(User, related_name='user')
#     phone = models.CharField(max_length=20, blank=True, default='')
#     street = models.CharField(max_length=100, default='', blank=True)
#     city = models.CharField(max_length=100, default='', blank=True)
#     country = models.CharField(max_length=100, default='', blank=True)
