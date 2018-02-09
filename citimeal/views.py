from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def item_page(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, "item.html", context)


def cart_page(request):
    if request.user.is_authenticated:
        try:
            cart_obj = Cart.objects.all().get(user=request.user)
            total=0
            for item in cart_obj.items.all():
                total+=item.price
            cart_obj.total = total
            cart_obj.save()
        except Cart.DoesNotExist:
            cart_obj = None
    else:
        cart_obj = None
    context = {
        'cart_obj' : cart_obj,
    }
    return render(request, "cart.html", context)


def cart_update(request):
    item_name = request.POST.get('item_name')
    if item_name is not None:
        if request.user.is_authenticated():
            try:
                cart_obj = Cart.objects.all().get(user=request.user)
                item_obj = Item.objects.get(item_name=item_name)
                # price = cart_obj.total + Item.objects.get(item_name=item_name).price
                # print(price)
                cart_obj.items.add(item_obj)
            except Cart.DoesNotExist:
                cart_obj = Cart.objects.create(user=request.user)
                item_obj = Item.objects.get(item_name=item_name)
                cart_obj.items.add(item_obj)
        else:
            return HttpResponse("<h1>Please login first<h1>")
    return redirect("cart")


def order_page(request):
    subject = 'Some subject'
    from_email = settings.DEFAULT_FROM_EMAIL
    message = 'This is my test message'
    recipient_list = ['mytest@gmail.com', 'kaman5624@gmail@gmail.com']
    html_message = '<h1>This is my HTML test</h1>'

    send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
    return HttpResponse('hello')
