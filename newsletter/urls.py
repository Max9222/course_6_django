from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import NewsletterCreateView

app_name = NewsletterConfig.name

urlpatterns = [
    path('create/<int:pk>/', NewsletterCreateView.as_view(), name='create'),
]