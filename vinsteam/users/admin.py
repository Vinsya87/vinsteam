from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'phone')}),
    )
    form = CustomUserChangeForm
    list_display = ('pk', 'username', 'first_name', 'last_name', 'email', 'password', 'phone', 'role')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('username',)
    empty_value_display = '-пусто-'

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        # Убираем поле "user_permissions" для не-суперпользователей и не-админа
        if not request.user.is_superuser and not request.user.groups.filter(name='Admin').exists():
            fieldsets = [
                (name, fieldset) for name,
                fieldset in fieldsets if 'user_permissions' not in fieldset['fields']]
        return fieldsets


admin.site.register(User, CustomUserAdmin)
