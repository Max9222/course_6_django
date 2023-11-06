from datetime import datetime
from smtplib import SMTPException

from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from main.models import Logs, Client, Message, Mailling


# def send_message_email(mailling_item: Mailling):
#     send_mail(
#         'Рассылка',
#         f'{mailling_item.message.head} ({mailling_item.message.body}) Приходите к нам на прием!',
#         settings.EMAIL_HOST_USER,   # Кто отправляет
#         ['maxoog@bk.ru']     # Список кому отправляем mailling_item.client.email


def send_mailling(mailling: Mailling):
    now = datetime.now().time()
    if mailling.start_to_send <= now <= mailling.stop_to_send:
        for client in mailling.client.all():
            try:
                send_mail(
                    mailling.message.head,
                    mailling.message.body,
                    settings.EMAIL_HOST_USER,
                    recipient_list=[client],
                    fail_silently=False
                )
                log = Logs.objects.create(
                    last_try=mailling.start_to_send,
                    status_try='Успешно',
                    mailling=mailling,
                    client=client.email
                )
                log.save()
                return log

            except SMTPException as error:
                log = Logs.objects.create(
                    last_try=mailling.time_to_send,
                    status_try='Ошибка',
                    mailling=mailling,
                    client=client.email,
                    answer=error
                )
                log.save()
                return log

