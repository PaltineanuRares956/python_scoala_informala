from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class MyUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username']
    add_fieldsets = (
        (None, {
            'classes': 'wide',
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')
        }
         ),
    )
    fieldsets = []


admin.site.register(User, MyUserAdmin)
