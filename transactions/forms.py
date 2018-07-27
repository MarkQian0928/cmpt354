from django import forms
from .models import transactionHistory

class transactionListForm(forms.ModelForm):
    class Meta:
        model = transactionHistory
        fields =  '__all__'