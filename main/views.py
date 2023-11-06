
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from django.shortcuts import render, get_object_or_404

from main.models import Client, Message, Mailling, Logs
from main.services import send_message_email


class ClientListView(ListView):
    model = Client

class ClientDetailView(DetailView):
    model = Client
    permission_required = 'main.client_view'

class ClientCreateView(CreateView):
    model = Client
    fields = ('fio', 'email', 'comment')
    success_url = reverse_lazy('main:client_list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ('fio', 'email', 'comment')
    success_url = reverse_lazy('main:client_list')

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('main:client_list')


class MessageListView(ListView):
    model = Message

class MessageDetailView(DetailView):
    model = Message
    permission_required = 'main.message_view'

class MessageCreateView(CreateView):
    model = Message
    fields = ('head', 'body')
    success_url = reverse_lazy('main:message_list')

class MessageUpdateView(UpdateView):
    model = Message
    fields = ('head', 'body')
    success_url = reverse_lazy('main:message_list')

class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('main:message_list')


class MaillingListView(ListView):
    model = Mailling


class MaillingDetailView(DetailView):
    model = Mailling
    permission_required = 'main.mailling_view'

class MaillingCreateView(CreateView):
    model = Mailling
    fields = ('start_to_send', 'stop_to_send', 'periodicity', 'is_active', 'client', 'message', 'user',)
    success_url = reverse_lazy('main:mailling_list')

class MaillingUpdateView(UpdateView):
    model = Mailling
    fields = ('start_to_send', 'stop_to_send', 'periodicity', 'is_active', 'client', 'message', 'user',)
    success_url = reverse_lazy('main:mailling_list')

class MaillingDeleteView(DeleteView):
    model = Mailling
    success_url = reverse_lazy('main:mailling_list')


class LogsListView(ListView):
    model = Logs



    # def get_success_url(self):
    #     return reverse('main:client_view', args=[self.kwargs.get('pk')])
    #
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['client'] = get_object_or_404(Client, pk=self.kwargs.get('pk'))
    #     return context_data
    #
    # def form_valid(self, form):
    #     obj = form.save()
    #     send_message_email(obj)
    #     return super().form_valid(form)

