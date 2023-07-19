from django.contrib import admin
from django.utils.html import format_html

from .models import Config


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['address', 'email', 'phone_number', 'logo']

