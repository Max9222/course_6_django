from newsletter.models import Newsletter
from django.core.mail import send_mail
from django.conf import settings


def send_newsletter_email(newsletter_item: Newsletter):
    send_mail(
        'Рассылка',
        f'{newsletter_item.name} ({newsletter_item.email}) Приходите к нам на прием!',
        settings.EMAIL_HOST_USER,
        [newsletter_item.client.email]
    )
