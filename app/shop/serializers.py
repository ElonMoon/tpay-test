from rest_framework import serializers
from drf_writable_nested.mixins import UniqueFieldsMixin
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import Tag, Product, ProductOption

__all__ = (
    'TagSerializer',
    'ProductOptionSerializer',
    'ProductSerializer',
)


class TagSerializer(UniqueFieldsMixin):
    class Meta:
        model = Tag
        fields = ('pk', 'name')


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ('pk', 'name', 'price')


class ProductSerializer(WritableNestedModelSerializer):
    option_set = ProductOptionSerializer(required=False, many=True)
    tag_set = TagSerializer(required=False, many=True)

    class Meta:
        model = Product
        fields = ('pk', 'name', 'option_set', 'tag_set')
