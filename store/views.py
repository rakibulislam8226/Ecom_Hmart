from http import client
from multiprocessing.connection import Client
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from . models import *


# Create your views here.
def thankyou(request):
    return render(request,'store/success.html')

def checkout(request):
    return render(request,'store/checkout.html')


def placeorder(request):
    if request.method=="POST":
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)
        cart=request.session.get('cart')
        country=request.POST.get('country')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        postcode=request.POST.get('postcode')
        phone=request.POST.get('phone')
        email=request.POST.get('email')

        payment_id=request.POST.get('order_id')
        payment=request.POST.get('payment')
        amount=request.POST.get('amount')

        order=Order(
            user=user,
            country=country,
            address=address,
            city=city,
            state=state,
            postcode=postcode,
            phone=phone,
            email=email,
            payment_id=payment_id,
            amount=amount,
        )
        order.save()

        for i in cart:
            a=int(cart[i]['quantity'])
            b=int(cart[i]['price'])

            total=(a*b)

            item=OrderItem(
                order=order,
                product=cart[i]['name'],
                image=cart[i]['image'],
                quantity=cart[i]['quantity'],
                price=cart[i]['price'],
                total=total,

            )
            item.save()
        return render(request,'store/placeorder.html')



#############################
@login_required(login_url="/authentication/logoutuser/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/authentication/logoutuser/")
def cart_detail(request):
    return render(request, 'store/cart_details.html')
#############################











































