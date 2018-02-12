from django.db import models
from django.contrib.auth.models import User
from items.models import Item

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True)
    items       = models.ManyToManyField(Item, blank=True)
    total_price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
