from django.contrib import admin
from .models import Todo, User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Todo)

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "username", "last_login", 'date_joined', 'is_staff']

admin.site.register(User, CustomUserAdmin)