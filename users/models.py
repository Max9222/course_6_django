from django.contrib.auth.models import AbstractUser
from django.db import models

from main.models import NULLABLE

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)

    is_active = models.BooleanField(max_length=20, verbose_name='Подтверждение', default=False)
    verify_code = models.CharField(max_length=50, verbose_name='Верификация')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
