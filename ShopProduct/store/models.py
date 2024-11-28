from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

from shopproduct.models import TimestampedModel


class Store(TimestampedModel):
    store_name = models.CharField(max_length=100)
    markup_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.store_name
