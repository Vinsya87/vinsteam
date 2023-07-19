from ckeditor_uploader.views import upload
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from .sitemaps import CategorySitemap, PageSitemap, PostSitemap

sitemaps = {
    'staticpages': PageSitemap,
    'staticposts': PostSitemap,
    'staticcategory': CategorySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main_url')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('', include('articles.urls', namespace='articles')),
    
    path('mail/', include('mail_post.urls', namespace='mail_post')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path('upload/', upload, name='ckeditor_upload'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)