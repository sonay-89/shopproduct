from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView
from .models import Store
from .serializers import StoreSerializer, StoreProductCountSerializer
from ..products.models import StoreProductCount

class StoreCreateListView(ListCreateAPIView):
    # TODO сейчас это доступно для всех. Надо чтобы только авторизованым.
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name','id']  # TODO убрать айди, добавить фильтры, чтобы позволить найти магазины, созданные в определенном промежутке
    ordering_fields = ['name', 'id']  # Позволяет сортировать по этим полям

    @extend_schema(
            summary="Get list of stores",
            description="Retrieve a list of stores, with optional filtering and ordering",
            responses={200: StoreSerializer(many=True)}
        )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class StoreProductCountViewSet(viewsets.ModelViewSet): # TODO переделать на апивью. Рассказать мне разницу между этим
    queryset = StoreProductCount.objects.all()
    serializer_class = StoreProductCountSerializer

# TODO я просил, сделать StoreView, придумай что он будет делать, класс должен наследоваться от APIView. у класса должен быть метод get, и над ним должна быть схема. проверь как отображается это со схемой и без в свагере
