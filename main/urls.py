from django.urls import path

from main.apps import MainConfig
from main.views import ClientListView, ClientDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_view'),
]
