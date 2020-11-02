from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class CategoryModel(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    TYPE =(
        ('classic', 'classic'),
        ('slim', 'slim'),
    )
    category = models.ForeignKey(CategoryModel,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField()
    type = models.CharField(max_length=10, choices=TYPE)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name