from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Store
from .serializers import StoreBaseSerializer, StoreDetailSerializer
from ..products.models import StoreProductCount, Product
from ..products.serializers import StoreProductBaseSerializer


class StoreCreateListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreBaseSerializer
    queryset = Store.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["owner", "store_name", "created_at", "updated_at"]
    ordering_fields = ["store_name", "id"]  # Позволяет сортировать по этим полям

    @extend_schema(
        summary="Get list of stores",
        description="Retrieve a list of stores, with optional filtering and ordering",
        responses={200: StoreBaseSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        user = request.user
        store_user = Store.objects.filter(owner=user)
        serializer = self.get_serializer(store_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StoreProductCountDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreProductBaseSerializer  # Явно указываем serializer_class для генерации документации

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    @extend_schema(  # Добавляем схему с помощью drf-spectacular
        summary="Получение информации о количестве продукта в магазине",
    )
    def get(self, request, *args, **kwargs):
        user = request.user
        store_product_counts = StoreProductCount.objects.filter(
            owner=user
        )  # Используем filter() для получения всех объектов
        serializer = self.get_serializer(store_product_counts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Получаем данные из запроса
        serializer = StoreProductBaseSerializer(data=request.data)

        if serializer.is_valid():

            product_name_str = serializer.validated_data["product_name"]
            store_name_str = serializer.validated_data["store_name"]

            product = get_object_or_404(Product, product_name=product_name_str)
            store = get_object_or_404(Store, store_name=store_name_str)

            # Создаем новую запись с добавлением пользователя
            store_product_count = StoreProductCount.objects.create(
                product_name=product,  # Передаем объект Product
                store_name=store,  # Передаем объект Store
                count=serializer.validated_data["count"],
                owner=request.user,
            )

            # Возвращаем успешный ответ с созданной записью
            response_serializer = StoreProductBaseSerializer(store_product_count)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, *args, **kwargs):
        store_product_count = get_object_or_404(StoreProductCount, id=id, username=request.user)
        serializer = self.get_serializer(store_product_count, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, *args, **kwargs):
        store_product_count = get_object_or_404(StoreProductCount, id=id, username=request.user)
        serializer = self.get_serializer(store_product_count, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        store_product_count = get_object_or_404(StoreProductCount, id=id, username=request.user)
        store_product_count.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoreDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Возвращаем только те магазины, которые принадлежат текущему пользователю
        return Store.objects.filter(owner=user)
