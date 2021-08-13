from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ['email', 'username', 'is_staff', 'is_admin', 'is_superuser']
    search_fields = ['email', 'username']


admin.site.register(Account, AccountAdmin)
