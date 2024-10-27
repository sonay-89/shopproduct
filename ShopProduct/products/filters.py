# import django_filters
# from django_filters import rest_framework as filters
# from ShopProduct.products.models import Product
#
# class ProductFilter(django_filters.FilterSet):
#     ordering = filters.OrderingFilter(
#         fields=(
#             ('name', 'name'),
#             ('price', 'price'),
#             ('store', 'store'),
#         ),
#     )
#
#     class Meta:
#         model = Product
#         fields = {
#             'name': ['exact'],
#             'price': ['lt', 'gt'],  # Фильтрация по цене
#             'store': ['exact'],     # Фильтрация по ID магазина
#         }