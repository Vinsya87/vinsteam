from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    USER = 'Пользователь'
    LEGAL_ENTITY = 'Юр. Лицо'

    ROLE_CHOICES = [
        (USER, 'User'),
        (LEGAL_ENTITY, 'Юр. Лицо')
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=USER)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    email = models.EmailField('Email', max_length=254, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
