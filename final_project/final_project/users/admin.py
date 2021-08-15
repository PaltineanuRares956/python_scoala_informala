from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
from .forms import CreateUserForm
# Register your models here.


class MyUserAdmin(UserAdmin):
    form = CreateUserForm
    list_display = ['email', 'username', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username']
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')
        }
         ),
    )
    list_filter = []
    fieldsets = [
        # (None, {'fields': ['email', 'username', 'password']}),
        # (('Permissions'), {'fields': ['is_staff', 'is_superuser']})
    ]


admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
