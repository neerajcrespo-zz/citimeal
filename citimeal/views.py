import random
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import AddressForm, LoginForm, RegisterForm

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        return redirect("/login/")
    return render(request, "accounts/register.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Error")
    return render(request, "accounts/login.html", {"form":form})

def logout_page(request):
    logout(request)
    return redirect("/")


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
            return redirect("login")
    return redirect("cart")


def address_page(request):
    address_form = AddressForm(request.POST or None)
    context = {
        'address_form' : address_form,
    }
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    address = request.POST.get('address')

    if name is not None:
        obj = Address.objects.filter(user=request.user)
        if obj.count() == 0:
            print("create")
            Address.objects.create(user=request.user, name=name, phone=phone, address=address)
        else:
            print("delete")
            obj.delete()
            Address.objects.create(user=request.user, name=name, phone=phone, address=address)
        return redirect("summary")

    return render(request, "address.html", context)


def summary_page(request):
    cart_obj = Cart.objects.all().get(user=request.user)
    address = Address.objects.all().get(user=request.user)
    context = {
        'cart_obj' : cart_obj,
        'address' : address,
    }
    return render(request, "summary.html", context)


def order_page(request):
    order_id = random.randint(11111111,99999999)
    cart_items = Cart.objects.all().get(user=request.user).items.all()
    order_obj = Order.objects.create(order_id=order_id, user=request.user)

    for item in cart_items:
        order_obj.items.add(item)

    Cart.objects.filter(user=request.user).delete()

    # # Download the Python helper library from twilio.com/docs/python/install
    # from twilio.rest import Client
    #
    # # Your Account Sid and Auth Token from twilio.com/user/account
    # account_sid = ""
    # auth_token = ""
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages.create(
    #     "+91799115443",
    #     body="Thanks for order! Your order will be delivered soon.",
    #     from_="+14152379773",
    # )
    # print(message.sid)

    # subject = 'Some subject'
    # from_email = settings.DEFAULT_FROM_EMAIL
    # message = 'This is my test message'
    # recipient_list = ['mytest@gmail.com', 'kaman5624@gmail@gmail.com']
    # html_message = '<h1>This is my HTML test</h1>'
    #
    # send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
    return HttpResponse("Thanks for order! Your order will be delivered soon.")


def profile_page(request):
    try:
        user = Address.objects.all().get(user=request.user)
        order = Order.objects.all().get(user=request.user)
    except:
        user=None
        order=None
    context = {
        'user' : user,
        'order': order
    }
    return render(request, "profile.html", context)
