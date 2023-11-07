from django.urls import path

from main.apps import MainConfig
from main.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, MaillingListView, \
    MaillingCreateView, MaillingDetailView, MaillingUpdateView, MaillingDeleteView, LogsListView, MainView

app_name = MainConfig.name

urlpatterns = [
    path('', (MainView.as_view()), name='main'),

    path('client', ClientListView.as_view(), name='client_list'),   # Просмотр всех
    path('client/create/', ClientCreateView.as_view(), name='client_create'),   # Создание
    path('client/detail/<int:pk>/', ClientDetailView.as_view(), name='client_view'),   # Просмотр одного
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),   # Редактирование
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),   # Удаление

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/detail/<int:pk>/', MessageDetailView.as_view(), name='message_view'),
    path('message/edit/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('mailling/', MaillingListView.as_view(), name='mailling_list'),
    path('mailling/create/', MaillingCreateView.as_view(), name='mailling_create'),
    path('mailling/detail/<int:pk>/', MaillingDetailView.as_view(), name='mailling_view'),
    path('mailling/edit/<int:pk>/', MaillingUpdateView.as_view(), name='mailling_update'),
    path('mailling/delete/<int:pk>/', MaillingDeleteView.as_view(), name='mailling_delete'),

    path('logs/', LogsListView.as_view(), name='logs_list'),
]
