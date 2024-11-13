from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from ShopProduct.models import TimestampedModel
from ShopProduct.store.models import Store


class Product(TimestampedModel):
    name = models.CharField(max_length=100) #
    price = models.DecimalField(max_digits=20, decimal_places=2)
    # store = models.ManyToManyField('store.Store',through='StoreProductCount')

    def __str__(self):
        return self.name

class StoreProductCount(TimestampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    @property
    def price(self):
        return self.product.price