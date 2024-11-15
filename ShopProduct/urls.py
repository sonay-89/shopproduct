from django.contrib import admin
from django.urls import include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

from shopproduct.store.views import StoreProductCountDeleteUpdateDetailView
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
    path("store-product-counts/", StoreProductCountDeleteUpdateDetailView.as_view(), name="storeproductcount-list"),  #
    # Маршрут для детального просмотра, обновления и удаления по ID
    path("register/", RegisterView.as_view(), name="register"),
]
