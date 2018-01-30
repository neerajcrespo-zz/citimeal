from django.contrib import admin

from .models import User, Item, Order, Delivery, Account

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Account)
