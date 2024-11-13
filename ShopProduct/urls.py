
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

from ShopProduct.store.views import StoreProductCountDetailView
from ShopProduct.user.views import RegisterView

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
    path('register/', RegisterView.as_view(), name='register'),
    # вьюшка, которая содержит логику для регистрации пользователя.
    # Например, она может обрабатывать запросы, когда кто-то хочет создать новую учетную запись.
    path('user/', include('ShopProduct.user.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', include('ShopProduct.products.urls')),
    path('stores/', include('ShopProduct.store.urls')),
    path('store-product-counts/', StoreProductCountDetailView.as_view(), name='storeproductcount-list'),

    path('silk/', include('silk.urls', namespace='silk')),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
