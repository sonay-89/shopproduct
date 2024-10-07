
from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


from ShopProduct import views

router = DefaultRouter()
router.register(r'shop', views.ShopListView, basename='shop')
router.register(r'product', views.ProductListView, basename='product')


schema_view = get_schema_view(
    openapi.Info(
        title="Project API SHOP",
        default_version='v1',
        description="Для товара и магазинов",
        contact=openapi.Contact(email="aloy02102024@gmail.com"),
        license=openapi.License(name="End User License Agreement"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
