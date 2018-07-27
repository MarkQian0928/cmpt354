from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Retailer, VIP

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    password = auth_forms.ReadOnlyPasswordHashField(label="Password",
        help_text=" Raw passwords are not stored, so there is no way to see "
                  "this user's password, but you can change the password "
                  "using <a href=\"../password_reset/\">this form</a>.")

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password','street', 'city', 'country', 'phone')
    
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial["password"]

class RetailerForm(forms.ModelForm):
    class Meta:
        model = Retailer
        fields = ('retailerOrNot',)

class VIPForm(forms.ModelForm):
    class Meta:
        model = VIP
        fields = ('vipOrNot',)


