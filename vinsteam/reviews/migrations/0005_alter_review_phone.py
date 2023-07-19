# Generated by Django 4.2 on 2023-04-26 03:19

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, error_messages={'invalid': 'Пожалуйста, введите корректный номер телефона'}, max_length=128, null=True, region=None, verbose_name='Телефон'),
        ),
    ]
