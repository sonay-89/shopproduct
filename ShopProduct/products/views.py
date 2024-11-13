from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer

@extend_schema(
    request=ProductSerializer,
    responses={201: ProductSerializer, 200: ProductSerializer}) # TODO это лишнее

class ProductCreateListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'price', 'storeproductcount__store']  # Позволяет фильтровать по этим полям
    ordering_fields = ['name', 'price']  # Позволяет сортировать по этим полям
