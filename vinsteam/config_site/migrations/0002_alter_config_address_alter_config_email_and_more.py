# Generated by Django 4.2 on 2023-04-26 05:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('config_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='address',
            field=models.CharField(help_text='Адрес вашей компании или организации', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='config',
            name='email',
            field=models.EmailField(help_text='Email, на который будут приходить сообщения с сайта', max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='config',
            name='logo',
            field=models.ImageField(blank=True, help_text='Изображение логотипа вашей компании или организации', upload_to='media/', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='config',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Телефонный номер, отображаемый на сайте', max_length=128, region=None, verbose_name='Телефонный номер'),
        ),
    ]