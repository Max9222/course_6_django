# Generated by Django 4.2.6 on 2023-11-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='client',
            field=models.ManyToManyField(to='main.client', verbose_name='Кому'),
        ),
    ]