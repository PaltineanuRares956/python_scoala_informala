from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class UserAdmin(UserAdmin):
    list_display = ['email', 'username', 'is_staff', 'is_admin', 'is_superuser']
    search_fields = ['email', 'username']


admin.site.register(User, UserAdmin)
