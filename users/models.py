from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    games = models.PositiveIntegerField(default=0, verbose_name='Количество сыгранных игр')
    percent_of_right_answers = models.FloatField(default=0, verbose_name='Процент правильных ответов')
    percent_of_wrong_answers = models.FloatField(default=0, verbose_name='Процент неправильных ответов')
