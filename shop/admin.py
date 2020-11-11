from django.contrib import admin
from .models import CategoryModel, Product, FabricModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(FabricModel)
class FabricAdmin(admin.ModelAdmin):
    list_display = ['fabric', 'slug']
    prepopulated_fields = {'slug': ('fabric',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
