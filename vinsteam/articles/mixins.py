from articles.models import Category, MenuItem
from django.db.models import Q
from django.views.generic.base import ContextMixin


class MenuView(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_items'] = MenuItem.objects.filter(is_active=True, is_main_menu=True).order_by('order')
        context['mobile_menu_items'] = MenuItem.objects.filter(is_active=True, is_mobile_menu=True).order_by('order')
        context['footer_menu_items'] = MenuItem.objects.filter(is_active=True, is_footer_menu=True).order_by('order')
        context['other_menu_items'] = MenuItem.objects.filter(is_active=True, is_other_menu=True).order_by('order')
        return context

