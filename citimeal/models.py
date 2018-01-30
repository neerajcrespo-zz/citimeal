from django.contrib.auth.models import User
from django.db import models

DELIVERY_STATUS_CHOICES = (
    ('shipped','Shipped'),
    ('delivered','Delivered'),
)

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
    image      = models.ImageField(upload_to="items/", null=True, blank=True)
    price      = models.IntegerField(null=True)
    active     = models.BooleanField(default=True)
    timestamp  = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.item_name)


class Order(models.Model):
    order_id  = models.CharField(max_length=120, null=True, blank=True)
    user      = models.ForeignKey(User)
    items     = models.ManyToManyField(Item)
    timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.order_id)


class Delivery(models.Model):
    order             = models.ForeignKey(Order)
    delivery_boy_name = models.CharField(max_length=120)
    status            = models.CharField(max_length=120, default='shipped', choices=DELIVERY_STATUS_CHOICES)
    pick_up_time      = models.TimeField()
    delivery_time     = models.TimeField()

    def __str__(self):
        return str(self.order)


class Account(models.Model):
    date  = models.DateField()
    order = models.ManyToManyField(Order)
    Total = models.IntegerField()

    def __str__(self):
        return str(self.date)
