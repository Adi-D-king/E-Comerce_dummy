from django.shortcuts import render
from .models import Products
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    products = Products.objects.all()

    return render(request,'shop/index.html',{'products':products})

def productView(request,product_id):
    product = get_object_or_404(Products,product_id=product_id)
    return render(request,'shop/productview.html',{'product':product})
