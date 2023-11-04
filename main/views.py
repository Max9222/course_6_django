
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from main.models import Client


class ClientListView(ListView):
    model = Client

class ClientDetailView(DetailView):
    model = Client
    permission_required = 'main.view_product'

class ClientCView(DetailView):
    model = Client
