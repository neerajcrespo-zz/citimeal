from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Item

class ItemListView(ListView):
    template_name = "items/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Item.objects.all()


class ItemDetailSlugView(DetailView):
    queryset = Item.objects.all()
    template_name = "items/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Item.objects.get(slug=slug, active=True)
        except Item.DoesNotExist:
            raise Http404("Not found..")
        except Item.MultipleObjectsReturned:
            qs = Item.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("not found")
        return instance
