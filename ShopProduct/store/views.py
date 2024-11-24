from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Store
from .serializers import StoreBaseSerializer, StoreDetailSerializer
from .. import settings
from ..products.models import StoreProductCount, Product
from ..products.serializers import StoreProductBaseSerializer
from ..settings import MAX_PRODUCTS_PER_OWNER


class StoreCreateListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreBaseSerializer
    queryset = Store.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["owner", "store_name", "created_at", "updated_at"]
    ordering_fields = ["store_name", "id"]  # Позволяет сортировать по этим полям

    def get(self, request, *args, **kwargs):
        user = request.user
        store_user = Store.objects.filter(owner=user)
        serializer = self.get_serializer(store_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@extend_schema(
    request=StoreProductBaseSerializer,  # Описываем входящие данные (POST/PUT)
    responses={200: StoreProductBaseSerializer, 201: StoreProductBaseSerializer},  # Описываем возможные ответы
    description="Endpoint to create, retrieve, update, and delete store product count.",
)
class StoreProductCountDetailUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreProductBaseSerializer

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get(self, request, id, *args, **kwargs):
        store_product_count = get_object_or_404(StoreProductCount, id=id, owner=request.user)
        serializer = self.get_serializer(store_product_count)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        store_product_count = get_object_or_404(StoreProductCount, id=id, owner=request.user)
        serializer = self.get_serializer(store_product_count, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, *args, **kwargs):
        store_product_count = get_object_or_404(StoreProductCount, id=id, owner=request.user)
        serializer = self.get_serializer(store_product_count, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        store_product_count = get_object_or_404(StoreProductCount, id=id, owner=request.user)
        store_product_count.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@extend_schema(
    request=StoreProductBaseSerializer,  # Описываем входящие данные (POST/PUT)
    responses={200: StoreProductBaseSerializer, 201: StoreProductBaseSerializer},  # Описываем возможные ответы
    description="Endpoint to create, retrieve, update, and delete store product count.",
)
class StoreProductCountListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreProductBaseSerializer

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        store_product_counts = StoreProductCount.objects.filter(owner=request.user)
        serializer = self.get_serializer(store_product_counts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            product_name = serializer.validated_data["product_name"]
            store_name = serializer.validated_data["store_name"]

            product = get_object_or_404(Product, product_name=product_name)
            store = get_object_or_404(Store, store_name=store_name)

            if StoreProductCount.objects.filter(owner=request.user, store_name=store).count() >= MAX_PRODUCTS_PER_OWNER:
                raise ValidationError("You can't have more than {} products in a store.".format(MAX_PRODUCTS_PER_OWNER))


            store_product_count = StoreProductCount.objects.create(
                product=product,
                store=store,
                count=serializer.validated_data["count"],
                owner=request.user,
            )
            response_serializer = self.get_serializer(store_product_count)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Возвращаем только те магазины, которые принадлежат текущему пользователю
        return Store.objects.filter(owner=user)
