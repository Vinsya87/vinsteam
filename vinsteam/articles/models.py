from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone


class MetaTagsMixin:
    def get_meta_tags(self):
        if hasattr(self, 'meta_title') and self.meta_title:
            meta_title = self.meta_title
        else:
            meta_title = None

        if hasattr(self, 'meta_description') and self.meta_description:
            meta_description = self.meta_description
        else:
            meta_description = None

        return {
            'meta_title': meta_title,
            'meta_description': meta_description
        }


class Category(models.Model, MetaTagsMixin):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    meta_title = models.CharField(
        max_length=255, blank=True,
        null=True, verbose_name='Meta Title')
    meta_description = models.TextField(
        blank=True, null=True, verbose_name='Meta Description')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('articles:post_list_by_category', args=[str(self.slug)])


class Post(models.Model, MetaTagsMixin):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    short_description = models.TextField(
        verbose_name='Короткое описание',
        blank=True, null=True)
    content_ckeditor = RichTextUploadingField(
        blank=True, null=True, verbose_name='Контент')
    main_content_block = models.ForeignKey(
        'ContentBlock',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='main_post',
        verbose_name='Главный блок контента')
    content_blocks = models.ManyToManyField(
        'ContentBlock', verbose_name='Блоки контента', blank=True)
    slug = models.SlugField(
        max_length=255, unique=True, verbose_name='URL')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name='Рубрика',
        null=False
    )
    order = models.PositiveIntegerField(
        'Сортировка', default=0)
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Изображение записи'
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    meta_title = models.CharField(
        max_length=255, blank=True,
        null=True, verbose_name='Meta Title')
    meta_description = models.TextField(
        blank=True, null=True, verbose_name='Meta Description')
    meta_keywords = models.CharField(
        max_length=255, blank=True,
        null=True, verbose_name='Meta Keywords')

    class Meta:
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:post_detail', args=[str(self.slug)])


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True, verbose_name='Включить меню')
    is_main_menu = models.BooleanField(
        default=False, verbose_name='Главное меню')
    is_mobile_menu = models.BooleanField(
        default=False, verbose_name='Мобильное меню')
    is_footer_menu = models.BooleanField(
        default=False, verbose_name='Футер меню')
    is_other_menu = models.BooleanField(
        default=False, verbose_name='Другое меню')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='menu_items',
        verbose_name='Рубрика',
        null=True, blank=True,
        help_text=('можно указать рубрику, и будут выведены все записи из нее')
        )

    class Meta:
        ordering = ('order',)
        verbose_name_plural = 'Меню'
        verbose_name = 'Меню'

    def __str__(self):
        return self.title


class Page(models.Model, MetaTagsMixin):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content_blocks = models.ManyToManyField(
        'ContentBlock', verbose_name='Блоки контента', blank=True)
    slug = models.SlugField(max_length=255,
                            unique=True, blank=True,
                            null=True, verbose_name='URL')
    content_ckeditor = RichTextUploadingField(
        blank=True, null=True, verbose_name='Контент')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Дата изменения')
    is_homepage = models.BooleanField(default=False, verbose_name='Главная страница')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    # Поля для SEO
    meta_title = models.CharField(
        max_length=255, blank=True,
        null=True, verbose_name='Meta Title')
    meta_description = models.TextField(
        blank=True, null=True, verbose_name='Meta Description')
    meta_keywords = models.CharField(
        max_length=255, blank=True,
        null=True, verbose_name='Meta Keywords')

    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.is_homepage:
            return reverse('main_url:main_index')
        else:
            return reverse('articles:page_detail', args=[str(self.slug)])


@receiver(pre_save, sender=Page)
def update_homepage(sender, instance, **kwargs):
    if instance.is_homepage:
        # Убедиться, что только одна страница может быть отмечена как главная
        Page.objects.exclude(pk=instance.pk).update(is_homepage=False)


class ContentBlock(models.Model):
    title = models.CharField(
        max_length=255, blank=True,
        null=True, verbose_name='Название блока')
    number = models.PositiveIntegerField(
        unique=True, verbose_name='Номер блока')
    content_ckeditor = RichTextUploadingField(verbose_name='Контент')
    css_class = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='CSS класс')
    div_id = models.CharField(
        max_length=255, unique=True, blank=True,
        null=True, verbose_name='ID div')

    class Meta:
        verbose_name_plural = 'Блоки контента'
        verbose_name = 'Блок контента'

    def __str__(self):
        return f'{self.title}'
