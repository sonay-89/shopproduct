from django.contrib.auth import get_user_model
from django.db import models

from shopproduct.models import TimestampedModel
from shopproduct.store.models import Store


class Product(TimestampedModel):
    product_name = models.CharField(max_length=100, unique=True)  #
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.product_name


class StoreProductCount(TimestampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="store_counts")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="product_counts")
    count = models.PositiveIntegerField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="product_counts")
    store_price = models.DecimalField(max_digits=20, decimal_places=2, editable=False, default=0)

    def save(self, *args, **kwargs):
        # Рассчитываем store_price на основе цены продукта и наценки магазина
        self.store_price = self.product.price + (self.product.price * self.store.markup_percentage / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} - {self.count} (Store: {self.store})"
