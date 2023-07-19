from articles.mixins import MenuView
from articles.models import Page
from articles.models import Post as ArticlePost
from articles.views import ArticleView
from banner.models import Slider
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.cache import caches
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_GET
from django.views.generic import ListView
from mail_post.views import FeedView
from reviews.mixins import ReviewMixin


class IndexView(MenuView, ReviewMixin, FeedView, ListView):
    template_name = 'index.html'
    model = ArticlePost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.all()
        posts = ArticleView().get_queryset().filter(
            category__id=1, is_published=True).order_by('order')[:3]
        special = ArticleView().get_queryset().filter(
            category__id=2, is_published=True).order_by('order')[:3]
        vodosnab = ArticleView().get_queryset().filter(
            category__id=3, is_published=True).order_by('order')[:5]
        page = get_object_or_404(Page, is_homepage=True)
        content_blocks = page.content_blocks.all()
        enabled_reviews = self.get_enabled_reviews()[:8]
        context.update(
                sliders=sliders,
                posts=posts,
                page=page,
                vodosnab=vodosnab,
                content_blocks=content_blocks,
                enabled_reviews=enabled_reviews,
                special=special,
                meta_tags=page.get_meta_tags()
                )
        return context


def paginator_page(request, page_pagi):
    # paginator = Paginator(page_pagi, settings.PER_PAGE)
    paginator = Paginator(page_pagi, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


@login_required
@staff_member_required
@require_GET
def clear_cache(request):
    cache = caches['default']
    cache.clear()
    return redirect('main_url:main_index')
