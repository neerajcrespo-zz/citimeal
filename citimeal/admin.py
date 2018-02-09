from django.contrib import admin

from .models import *

admin.site.register(Address)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Account)
