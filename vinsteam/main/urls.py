from django.urls import path
from main.views import IndexView, clear_cache

app_name = 'main_url'

urlpatterns = [
    path('', IndexView.as_view(), name='main_index'),
    path('clear_cache/', clear_cache, name='clear_cache'),
    ]
