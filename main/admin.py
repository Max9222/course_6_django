from django.contrib import admin

from main.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('id',)
