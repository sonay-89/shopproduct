# import django_filters
#
# from ShopProduct.products.models import Product
# from ShopProduct.store.models import Store
#
#
# class ProductFilter(django_filters.FilterSet):
#     class Meta:
#         model = Product
#         fields = {
#             'name': ['exact'],
#             'price': ['lt', 'gt'],   # Фильтрация по цене
#             'store': ['exact'],      # Фильтрация по ID магазина
#         }
#
# class StoreFilter(django_filters.FilterSet):
#     class Meta:
#         model = Store
#         fields = {
#             'name': ['exact'],
#         }

# TODO если не используется, удалить