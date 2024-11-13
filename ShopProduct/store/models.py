from django.db import models

from ShopProduct.models import TimestampedModel


class Store(TimestampedModel):
    name = models.CharField(max_length=100)
    # TODO сюда надо добавить юзера, и при создании магазина необходимо сюда прописывать поле этого юзера(брать из реквеста/jwt токена)
    def __str__(self):
        return self.name
