from django.db import models


class InventoryItem(models.Model):
    name = models.CharField(max_length=1024, unique=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    code = models.CharField(max_length=255)

    inventoryitems = models.ManyToManyField(InventoryItem)

    def __str__(self):
        return self.code
