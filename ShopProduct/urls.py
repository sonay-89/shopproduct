from django.contrib import admin
from django.urls import include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

from shopproduct.store.views import StoreProductCountDetailUpdateDeleteView, StoreProductCountListCreateView
from shopproduct.user.views import RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("shopproduct.user.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("products/", include("shopproduct.products.urls")),
    path("stores/", include("shopproduct.store.urls")),
    path('store-product-counts-detail/<int:id>/', StoreProductCountDetailUpdateDeleteView.as_view(), name='store-product-detail'),
    path('store-product-counts/', StoreProductCountListCreateView.as_view(), name='store-product-list-create'),
    path("register/", RegisterView.as_view(), name="register"),
]
