from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматически заполняется при создании объекта
    updated_at = models.DateTimeField(auto_now=True)  # Автоматически обновляется при каждом сохранении объекта

    class Meta:
        abstract = True
