
from django.urls import path, include

from shopproduct.store.views import StoreCreateListView

urlpatterns = [
    path('', StoreCreateListView.as_view(), name='store-list'), # TODO следи за неймингом
    # TODO добавить еще маршрут, для аптейда, удаления, чтения конкретного магазина. Это магазин должен быть доступен только для юзера, если он его создал.
]

# example Это изменения Сони
# example (тут изменения)