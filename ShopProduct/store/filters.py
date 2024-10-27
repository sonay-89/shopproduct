# import django_filters
# from rest_framework import filters
#
# from ShopProduct.store.models import Store
#
#
# class StoreFilter(django_filters.FilterSet):
#     ordering = filters.OrderingFilter(fields=(('name', 'name'), ('created_at', 'created_at'),),)
#
#     class Meta:
#         model = Store
#         fields = {
#             'name': ['exact'],
#         }