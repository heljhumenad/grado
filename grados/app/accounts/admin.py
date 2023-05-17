from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from grados.app.accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = get_user_model
    list_display = [
        "first_name",
        "last_name",
        "email",
        "username",
    ]
