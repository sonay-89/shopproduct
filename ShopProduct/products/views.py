from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductBaseSerializer


class ProductCreateListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductBaseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["id", "price"]  # Позволяет фильтровать по этим полям
    ordering_fields = ["id", "price"]  # Позволяет сортировать по этим полям
