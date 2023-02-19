from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    number_phone = models.CharField(verbose_name='Номер телефона', max_length=20)
    mail = models.EmailField(verbose_name='Почта')
    photo = models.ImageField('Фотография', upload_to='user_photo/%Y/%m/%d/', null=True)

