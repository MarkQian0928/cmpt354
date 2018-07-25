from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
<<<<<<< HEAD
    # username = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    # first_name = forms.CharField(required=False)
    # last_name = forms.CharField(required=False)
    password = auth_forms.ReadOnlyPasswordHashField(label="Password",
        help_text=" Raw passwords are not stored, so there is no way to see "
                  "this user's password, but you can change the password "
                  "using <a href=\"../password_reset/\">this form</a>.")

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password','street', 'city', 'country', 'phone')
    
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
=======
    # class Meta:
    #     model = CustomUser
    #     fields = ('username', 'email', 'password', 'first_name')

    password = auth_forms.ReadOnlyPasswordHashField(label="Password",
        help_text="Raw passwords are not stored, so there is no way to see "
                  "this user's password, but you can change the password "
                  "using <a href=\"password/\">this form</a>.")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name')

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
>>>>>>> 9f7f047a4a7b98f942c7baadf01ca86af883b03b
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
<<<<<<< HEAD
        return self.initial["password"]
=======
        return self.initial["password"]
>>>>>>> 9f7f047a4a7b98f942c7baadf01ca86af883b03b
