# Generated by Django 4.2.6 on 2023-11-05 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_message_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='client',
        ),
    ]
