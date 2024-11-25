from django.urls import path

from shopproduct.products.views import ProductCreateListView

urlpatterns = [
    path("", ProductCreateListView.as_view(), name="product-create-list"),  # Добавляем маршрут для ProductListView
]
