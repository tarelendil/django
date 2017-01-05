from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from .models import Product, Image


def index(request):
    product_list=Product.objects.all()
    cart_sum = 0
    for product in product_list:
        cart_sum = cart_sum+product.in_cart_number
    context = {'product_list': product_list, 'cart_sum': cart_sum}
    return render(request, 'shop/index.html', context)


def bought(request):
    product_list=Product.objects.filter(in_cart_number__gte=1)
    total_price_dict={}
    for item in product_list:
        total_price_dict[item.id]=item.in_cart_number*item.official_price
    context = {'product_list': product_list, 'total_price_dict': total_price_dict}
    return render(request, 'shop/cart.html', context)


def add_to_cart(request):
    selected_prod = get_object_or_404(Product, pk=request.POST['product_bought'])

    product = get_object_or_404(Product, pk=selected_prod.id)
    product.in_cart_number = F('in_cart_number')+1
    product.save()
    return HttpResponseRedirect(reverse('shop:index'))
