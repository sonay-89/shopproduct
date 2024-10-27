
from django.contrib import admin
from django.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

from ShopProduct.store.views import StoreProductCountViewSet
from ShopProduct.user.views import UserInfoView, RegisterView

# Создаем представления для списка и детального просмотра
store_product_count_list = StoreProductCountViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

store_product_count_detail = StoreProductCountViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



# это удалить
schema_view = get_schema_view(
    openapi.Info(
        title="Project API SHOP",
        default_version='v1',
        description="Для товара и магазинов",
        contact=openapi.Contact(email="aloy02102024@gmail.com"),
        license=openapi.License(name="End User License Agreement"),
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # TODO распределить нормально по группам
    path('products/', include('ShopProduct.products.urls')),
    path('stores/', include('ShopProduct.store.urls')),
    path('user/', include('ShopProduct.user.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('store-product-counts/', store_product_count_list, name='storeproductcount-list'), # TODO перенести
    # Маршрут для детального просмотра, обновления и удаления по ID
    path('store-product-counts/<int:pk>/', store_product_count_detail, name='storeproductcount-detail'),
    path('silk/', include('silk.urls', namespace='silk')),
    path('api/v1/drf-auth/', include('rest_framework.urls')), # TODO что это и зачем
    path('accounts/', include('django.contrib.auth.urls')), # TODO что это и зачем
    path('register/', RegisterView.as_view(), name='register'), # TODO что это и зачем

]
