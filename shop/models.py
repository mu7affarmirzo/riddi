from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from account.models import Account

class CategoryModel(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class FabricModel(models.Model):
    fabric = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)
    index = models.BooleanField(default=False)

    class Meta:
        ordering = ('price', )
        verbose_name = 'fabric'
        verbose_name_plural = 'fabrics'

    def __str__(self):
        return self.fabric


class Product(models.Model):
    TYPE =(
        ('classic', 'classic'),
        ('slim', 'slim'),
    )
    category = models.ForeignKey(CategoryModel,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    fabric = models.ForeignKey(FabricModel,
                                 related_name='fabrics', blank=True, null=True,
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

class OrderProduct(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.item.quantity} of {self.item.title}"

class Order(models.Model):
    # settings.AUTH_USER_MODEL
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
