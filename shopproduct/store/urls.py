from django.urls import path, include

from shopproduct.store.views import StoreCreateListView, StoreDetailUpdateDeleteView

urlpatterns = [
    path("", StoreCreateListView.as_view(), name="store-list"),
    path("<int:pk>/", StoreDetailUpdateDeleteView.as_view(), name="store-detail"),
]