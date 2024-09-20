from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Index_ecom1")
    return render(request,'Main_ecom1/index.html')