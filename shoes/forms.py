from django import forms
from django.contrib.auth import forms as auth_forms
from .models import Shoes

class ShoesCreationForm(forms.ModelForm):
    class Meta:
        model = Shoes
        # fields = ('brand','category', 'size', 'gender', 'color', 'description', 'price', 'numOfAvail',)
        fields = '__all__'