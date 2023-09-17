from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm, ImageChangeForm
# Register your models here.

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = [CustomUserCreationForm, ImageChangeForm]
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_superuser",
        "image"
    ]

admin.site.register(CustomUser, CustomUserAdmin)