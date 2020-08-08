from django.contrib import admin

# Register your models here.
from .models import Tag, Product, ProductOption
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    pass
