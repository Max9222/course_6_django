from smtplib import SMTPException

from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from main.models import Logs, Message


def send_message_email(message_item: Message):
    send_mail(
        'Рассылка',
        f'{message_item.head} ({message_item.body}) Приходите к нам на прием!',
        settings.EMAIL_HOST_USER,   # Кто отправляет
        [message_item.email]     # Список кому отправляем
    )

# def send_mailling(mailling):
#     now = timezone.localtime(timezone.now())
#     if mailling.start_to_send <= now <= mailling.stop_to_send:
#         for client in mailling.client.all():
#             try:
#                 send_mail(
#                     mailling.message.head,
#                     mailling.message.body,
#                     settings.EMAIL_HOST_USER,
#                     recipient_list=[client],
#                     fail_silently=False
#                 )
#                 log = Logs.objects.create(
#                     last_try=mailling.start_to_send,
#                     status_try='Успешно',
#                     mailling=mailling,
#                     client=client.email
#                 )
#                 log.save()
#                 return log
#
#             except SMTPException as error:
#                 log = Logs.objects.create(
#                     last_try=mailling.time_to_send,
#                     status_try='Ошибка',
#                     mailling=mailling,
#                     client=client.email,
#                     answer=error
#                 )
#                 log.save()
#                 return log

