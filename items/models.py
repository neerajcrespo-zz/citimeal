from django.db import models

class Item(models.Model):
    item_id         = models.CharField(max_length=120)
    item_name       = models.CharField(max_length=120)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return self.item_id
