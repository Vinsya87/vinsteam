from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView
from mail_post.views import FeedView

from articles.mixins import MenuView
from articles.models import Category as ArticleCategory
from articles.models import Page
from articles.models import Post as ArticlePost


class ArticleView(ListView):
    model = ArticlePost
    context_object_name = 'posts'
    template_name = 'catalog/article_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = ArticlePost.objects.all()
        return queryset


class PostDetailView(
        MenuView,
        FeedView,
        DetailView):
    """Детали поста"""
    model = ArticlePost
    context_object_name = 'post'

    # @method_decorator(cache_page(30 * 24 * 60 * 60))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_template_names(self):
        category = self.object.category
        if category.slug == 'specialisty':
            return ['articles/article_detail_specialisty.html']
        elif category.slug == 'second_category':
            return ['articles/second_category_post_detail.html']
        else:
            return ['articles/article_detail.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self.object, 'get_meta_tags'):
            context['meta_tags'] = self.object.get_meta_tags()
        return context


class PageDetailView(
        MenuView,
        FeedView,
        DetailView):
    """Детали страницы"""
    model = Page
    template_name = 'articles/page_detail.html'
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self.object, 'get_meta_tags'):
            context['meta_tags'] = self.object.get_meta_tags()
        return context


class PostListByCategory(
        MenuView,
        FeedView,
        ListView):
    """Список постов категории"""
    model = ArticlePost
    context_object_name = 'posts'

    def get_template_names(self):
        category_slug = self.kwargs['category_slug']
        if category_slug == 'specialisty':
            return ['articles/post_list_special.html']
        elif category_slug == 'price':
            return ['articles/post_list_price.html']
        else:
            return ['articles/article_list.html']

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = ArticleCategory.objects.get(slug=category_slug)
        queryset = ArticlePost.objects.filter(category=category, is_published=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        category = ArticleCategory.objects.get(slug=category_slug)
        context['category'] = category
        if hasattr(category, 'get_meta_tags'):
            context['meta_tags'] = category.get_meta_tags()
        return context
