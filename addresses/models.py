from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user            = models.ForeignKey(User, null=True, blank=True)
    full_name       = models.CharField(max_length=120, default='')
    mobile_no       = models.CharField(max_length=120, default='')
    address_line_1  = models.CharField(max_length=120)
    address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    city            = models.CharField(max_length=120)
    country         = models.CharField(max_length=120, default='India')
    state           = models.CharField(max_length=120)
    postal_code     = models.CharField(max_length=120)

    def __str__(self):
        return str(self.user)
