# Generated by Django 4.2 on 2023-04-26 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config_site', '0004_alter_config_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='logo',
        ),
    ]
