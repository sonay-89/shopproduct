from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    number= models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()


    def __str__(self):
        return self.name
