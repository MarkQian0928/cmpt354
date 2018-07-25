from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)