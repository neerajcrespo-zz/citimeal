from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    user    = models.ForeignKey(User)
    phone   = models.CharField(max_length=120)
    address = models.CharField(max_length=120)

    def __str__(self):
        return str(self.user)


class Item(models.Model):
    item_id    = models.CharField(max_length=120)
    item_name  = models.CharField(max_length=120, null=True, blank=True)
    desciption = models.CharField(max_length=120)

    def __str__(self):
        return str(self.item_name)


class Order(models.Model):
    user  = models.ForeignKey(User)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return str(self.user)
