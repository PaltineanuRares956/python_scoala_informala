from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    default_site = 'AdminSite'
