from rest_framework import permissions
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.\
        prefetch_related('tag_set', 'option_set').\
        all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
