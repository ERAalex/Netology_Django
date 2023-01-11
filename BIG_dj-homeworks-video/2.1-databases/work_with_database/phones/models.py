from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(null=False, verbose_name='Название модели', max_length=50)
    price = models.IntegerField(default=0, verbose_name='Цена')
    image = models.ImageField(null=True, blank=True, upload_to='static/img/models', verbose_name='Мини-изображение')
    release_date = models.DateTimeField('Дата продажи')
    lte_exists = models.BooleanField('Доступно для продажи?', default=False)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Телефоны'
        verbose_name_plural = 'Телефоны'