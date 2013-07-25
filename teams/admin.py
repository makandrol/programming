__author__ = 'Olya'

from teams.models import Customer, Manager, Developer
from django.contrib import admin


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['name']})
    ]
    list_display = ['name']

admin.site.register(Customer, CustomerAdmin)


class ManagerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['name']})
    ]
    list_display = ['name']

admin.site.register(Manager, ManagerAdmin)


class DeveloperAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['name', 'qualification', 'hour_cost', 'isFree']})
    ]
    list_display = ['name', 'qualification', 'hour_cost', 'isFree']

admin.site.register(Developer, DeveloperAdmin)