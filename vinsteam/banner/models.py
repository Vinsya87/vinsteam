from django.core.exceptions import ValidationError
from django.db import models


class Slider(models.Model):
    title = models.CharField(
        'Заголовок', max_length=255)
    text = models.TextField()
    link = models.CharField(
        'Ссылка на запись или новость',
        max_length=255,
        blank=True)
    slug = models.SlugField(
        max_length=255, verbose_name='URL-на всякий', blank=True)
    image = models.ImageField('Изображение большое', upload_to='sliders/')
    image_mobile = models.ImageField('Изображение на мобильном', upload_to='sliders/',blank=True)
    header_type = models.CharField(
        'Выбрать тип заголовка (H1 должен быть один)',
        choices=(('h1', 'H1'), ('h2', 'H2')),
        default='h2',
        max_length=2)
  
    class Meta:
        verbose_name_plural = 'Баннеры'

    def has_h1(self):
        if self.header_type == 'h1':
            return Slider.objects.filter(header_type='h1').exclude(pk=self.pk).exists()
        return Slider.objects.filter(header_type='h1').exists()

    def clean(self):
        if self.header_type == 'h1' and self.has_h1():
            raise ValidationError('Заголовок H1 уже существует. На слайдерах может быть только один h1')

    def __str__(self):
        return self.title
