from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from grados.app.accounts.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = get_user_model
    # add_form = forms.CustomUserCreationForm
    # form = forms.CustomUserChangeForm
    list_display = [
        'first_name', 'last_name',
        'email', 'username',
    ]
