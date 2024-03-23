from django.shortcuts import render
from django.http import JsonResponse
from OnlineApp.models import Product, Order


# Create your views here.
def store(request):
    product=Product.objects.all()
    context={'products':product}
    return render(request,'store/store.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}

    context={'items':items,'order':order}
    return render(request,'store/cart.html',context)
def chekout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}

    context={'items':items,'order':order}

    return render(request,'store/checkout.html',context)


def updateItem(request):
    return JsonResponse('Item added',safe=False)