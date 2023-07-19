from django.db import models


class Config(models.Model):
    phone_number = models.CharField(
        max_length=18,
        verbose_name='Телефонный номер',
        blank=True,
        null=True,
        help_text='Телефонный номер, отображаемый на сайте'
    )
    phone_url = models.CharField(
        max_length=15,
        verbose_name='Телефон ссылка',
        blank=True,
        null=True,
        help_text='Телефонный номер, ссылка, формат: +73822908070'
    )
    phone_number_two = models.CharField(
        max_length=18,
        verbose_name='Телефонный номер - 2',
        blank=True,
        null=True,
        help_text='Телефонный номер, отображаемый на сайте'
    )
    phone_two_url = models.CharField(
        max_length=15,
        verbose_name='Телефон ссылка - 2',
        blank=True,
        null=True,
        help_text='Телефонный номер, ссылка, формат: +73822908070'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True,
        null=True,
        help_text='Адрес вашей компании или организации'
    )
    email = models.EmailField(
        verbose_name='Email',
        blank=True,
        null=True,
        help_text='Email, на который будут приходить сообщения с сайта'
    )
    email_site = models.EmailField(
        verbose_name='Email',
        blank=True,
        null=True,
        help_text='Email, который отображается на сайте'
    )
    logo = models.ImageField(
        upload_to='media/',
        verbose_name='Логотип',
        help_text='Изображение логотипа вашей компании или организации',
        blank=True,
        null=True,
    )
    telegram = models.CharField(
        max_length=255, verbose_name='телеграм ссылка',
        blank=True, null=True)
    telegram_img = models.ImageField(
        upload_to='social_icons/', verbose_name='телеграм иконка',
        blank=True, null=True)
    whatsapp = models.CharField(
        max_length=255, verbose_name='ватсап ссылка',
        blank=True, null=True)
    whatsapp_img = models.ImageField(
        upload_to='social_icons/', verbose_name='ватсап иконка',
        blank=True, null=True)
    instagram = models.CharField(
        max_length=255, verbose_name='инстаграм ссылка',
        blank=True, null=True)
    instagram_img = models.ImageField(
        upload_to='social_icons/', verbose_name='инстаграм иконка',
        blank=True, null=True)
    vk = models.CharField(
        max_length=255, verbose_name='вк ссылка',
        blank=True, null=True)
    vk_img = models.ImageField(
        upload_to='social_icons/', verbose_name='вк иконка',
        blank=True, null=True)
    facebook = models.CharField(
        max_length=255, verbose_name='фэйсбук ссылка',
        blank=True, null=True)
    facebook_img = models.ImageField(
        upload_to='social_icons/', verbose_name='фэйбук иконка',
        blank=True, null=True)
    other = models.CharField(
        max_length=255, verbose_name='другая ссылка',
        blank=True, null=True)
    other_img = models.ImageField(
        upload_to='social_icons/', verbose_name='другая иконка',
        blank=True, null=True)
    random = models.CharField(
        max_length=255, verbose_name='другая-2 ссылка',blank=True, null=True)
    random_img = models.ImageField(
        upload_to='social_icons/', verbose_name='другая-2 иконка',
        blank=True, null=True)

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return self.address

