from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator


class ItemQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class ItemManager(models.Manager):
    def get_queryset(self):
        return ItemQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None



class Item(models.Model):
    item_name       = models.CharField(max_length=120)
    item_id         = models.CharField(max_length=120, null=False, blank=False)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image           = models.ImageField(upload_to='items/', null=True, blank=True)
    active          = models.BooleanField(default=True)

    objects = ItemManager()

    def get_absolute_url(self):
        return "/items/{slug}/".format(slug=self.slug)

    def __str__(self):
        return self.item_name


def item_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(item_pre_save_receiver, sender=Item)
