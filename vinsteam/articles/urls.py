from articles.views import (ArticleView, PageDetailView, PostDetailView,
                            PostListByCategory)
from django.urls import path

app_name = 'articles'

urlpatterns = [
    path('', ArticleView.as_view(), name='article_list'),
    path('<slug:slug>/', PageDetailView.as_view(), name='page_detail'),
    path(
        'article/<category_slug>/',
        PostListByCategory.as_view(),
        name='post_list_by_category'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
