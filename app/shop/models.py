from django.db import models

__all__ = (
    'Tag',
    'Product',
    'ProductOption',
)


class Tag(models.Model):
    name = models.CharField(verbose_name='태그명', unique=True, max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='상품명', max_length=100)
    tag_set = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(
        Product, verbose_name='상품',
        related_name='option_set', related_query_name='option', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='옵션명', max_length=100)
    price = models.IntegerField(verbose_name='가격', default=0)

    def __str__(self):
        return self.name
