from django.conf.urls import url

from .views import ItemListView, ItemDetailSlugView

urlpatterns = [
    url(r'^$', ItemListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ItemDetailSlugView.as_view()),
]
