from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse

from main.models import Client
from newsletter.models import Newsletter
from newsletter.services import send_newsletter_email


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = ('client', 'name', 'email', 'comment',)

    def get_success_url(self):
        return reverse('main:client_view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['client'] = get_object_or_404(Client, pk=self.kwargs.get('pk'))
        return context_data

    def form_valid(self, form):
        obj = form.save()
        send_newsletter_email(obj)
        return super().form_valid(form)
