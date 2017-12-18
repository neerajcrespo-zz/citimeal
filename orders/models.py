from django.db import models
from django.contrib.auth.models import User
from addresses.models import Address
from carts.models import Cart

class Order(models.Model):
    user                = models.ForeignKey(User, null=True, blank=True)
    order_id            = models.CharField(max_length=120, blank=True)
    shipping_address    = models.ForeignKey(Address, related_name="shipping_address",null=True, blank=True)
    cart                = models.ForeignKey(Cart)
    total_price         = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.user)
