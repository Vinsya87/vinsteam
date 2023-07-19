from articles.models import Category, ContentBlock, MenuItem, Page, Post
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.urls import reverse
from reversion.admin import VersionAdmin

# from django.utils.html import format_html

admin.site.site_header = "Панель управления TomVod"
admin.site.site_title = "Админка сайта TomVod"


@admin.register(Category)
class CategoryAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'id')
    search_fields = ('name',)

    class Media:
        js = ('js/admin_js.js',)


class PostBlockInline(admin.TabularInline):
    model = Post.content_blocks.through
    verbose_name_plural = 'Блоки контента на записи'


class PostAdmin(VersionAdmin):
    list_display = (
        'title', 'category', 'is_published',
        'slug', 'order', 'created_at')
    list_filter = ('category', 'created_at')
    list_editable = ('slug', 'order', 'is_published')
    search_fields = ('title', 'content_ckeditor')
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 40})},
    }

    fieldsets = [
        ('Основные данные', {'fields': (
         'title', 'slug', 'is_published', 'short_description',
         'category', 'main_content_block', 'content_ckeditor',
         'image', 'created_at', 'order')}),
        ('SEO', {'fields': ('meta_title',
                            'meta_description', 'meta_keywords')}),
    ]

    inlines = [PostBlockInline]

    class Media:
        js = ('js/admin_js.js',)

    def view_on_site(self, obj):
        return reverse('articles:post_detail', args=[obj.slug])

    list_display_links = ('title', 'category')


admin.site.register(Post, PostAdmin)


class PageBlockInline(admin.TabularInline):
    model = Page.content_blocks.through
    verbose_name_plural = 'Блоки контента на странице'


@admin.register(Page)
class PageAdmin(VersionAdmin):
    list_display = ('title', 'is_homepage',
                    'is_published', 'slug',
                    'id', 'created_at')
    list_editable = ('slug', 'is_published')
    list_filter = ('created_at',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_as = True

    inlines = [PageBlockInline]

    fieldsets = [
        ('Основные данные', {'fields': (
            'title', 'is_homepage',
            'is_published', 'slug',
            'content_ckeditor')}),
        ('SEO', {'fields': (
            'meta_title', 'meta_description', 'meta_keywords')})
    ]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 40})},
    }

    class Media:
        js = ('js/admin_js.js',)

    # formfield_overrides = {
    #     models.TextField: {'widget': CKEditorUploadingWidget},
    # }

    def view_on_site(self, obj):
        return reverse('articles:page_detail', args=[obj.slug])

    # def get_content_preview(self, obj):
    #     return format_html(obj.content_ckeditor[:200])

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == 'content_blocks':
    #         kwargs['widget'] = admin.widgets.FilteredSelectMultiple(
    #             db_field.verbose_name,
    #             False,
    #         )
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(MenuItem)
class MenuItemAdmin(VersionAdmin):
    list_display = (
        'title', 'url',
        'order', 'is_active',
        'is_main_menu', 'is_mobile_menu',
        'is_footer_menu', 'is_other_menu')
    list_editable = (
        'url', 'order',
        'is_active', 'is_main_menu',
        'is_mobile_menu', 'is_footer_menu',
        'is_other_menu')
    search_fields = ('title', 'url')


@admin.register(ContentBlock)
class ContentBlockAdmin(VersionAdmin):
    list_display = ('title', 'number', 'css_class', 'div_id')
