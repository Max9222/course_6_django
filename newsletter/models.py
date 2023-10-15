from django.db import models


class Newsletter(models.Model):
    client = models.ForeignKey('main.Client', on_delete=models.CASCADE, verbose_name='клиент')

    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(max_length=150, verbose_name='контактный email')
    comment = models.TextField(verbose_name='комментарий')

    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} от {self.email}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
