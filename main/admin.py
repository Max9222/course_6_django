from django.contrib import admin

from main.models import Client, Logs, Message, Mailling

admin.site.register(Client)
admin.site.register(Logs)
admin.site.register(Message)
admin.site.register(Mailling)

