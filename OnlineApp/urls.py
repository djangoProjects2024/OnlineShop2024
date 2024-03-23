from django.urls import path

from OnlineApp import views

urlpatterns = [
    path('',views.store,name='store'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.chekout,name='checkout'),
    path('update_item',views.updateItem,name='updateItem'),
]