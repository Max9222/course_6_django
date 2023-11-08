
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy

from django.http import Http404

from main.forms import ClientForm, MessageForm, MaillingForm
from main.models import Client, Message, Mailling, Logs
from main.services import send_mailling

from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная'

        return context_data


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список клиентов'
        return context_data

    def get_queryset(self):
        if self.request.user.is_staff:
            return Client.objects.all()
        queryset = Client.objects.filter(mailling__user=self.request.user)
        return queryset

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    permission_required = 'main.client_view'

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    # fields = ('fio', 'email', 'comment')
    success_url = reverse_lazy('main:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    # fields = ('fio', 'email', 'comment')
    success_url = reverse_lazy('main:client_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('main:client_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список сообщений'
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Message.objects.all()
        queryset = Message.objects.filter(user=self.request.user)
        return queryset

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    permission_required = 'main.message_view'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    # fields = ('head', 'body')
    success_url = reverse_lazy('main:message_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    # fields = ('head', 'body')
    success_url = reverse_lazy('main:message_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('main:message_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MaillingListView(LoginRequiredMixin, ListView):
    model = Mailling

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список рассылок'
        return context

class MaillingDetailView(LoginRequiredMixin, DetailView):
    model = Mailling
    permission_required = 'main.mailling_view'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object

class MaillingCreateView(LoginRequiredMixin, CreateView):
    model = Mailling
    form_class = MaillingForm
    # fields = ('start_to_send', 'stop_to_send', 'periodicity', 'is_active', 'client', 'message', 'user',)
    permission_required = 'main:mailling_list'

    def form_valid(self, form):
        obj = form.save()
        send_mailling(obj)
        return super().form_valid(form)


class MaillingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailling
    form_class = MaillingForm
    # fields = ('start_to_send', 'stop_to_send', 'periodicity', 'is_active', 'client', 'message', 'user',)
    success_url = reverse_lazy('main:mailling_list')

    def has_permission(self):
        obj = self.get_object()
        if self.request.user == obj.user or self.request.user.is_staff:
            return True
        return super().has_permission()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MaillingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailling
    success_url = reverse_lazy('main:mailling_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class LogsListView(LoginRequiredMixin, ListView):
    model = Logs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отчет об отправленных рассылках'
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Logs.objects.all()
        queryset = Logs.objects.filter(mailling__user=self.request.user)
        return queryset



