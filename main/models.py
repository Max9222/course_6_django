from django.db import models

NULLABLE = {'blank': True, 'null':True}

class Client(models.Model):
    email = models.EmailField(verbose_name='контактный email', unique=True)
    name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий')
    def __str__(self):
        return f'{self.email} {self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
