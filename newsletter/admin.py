from django.contrib import admin

from  newsletter.models import Newsletter

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('client', 'email', )
    list_filter = ('client',)

