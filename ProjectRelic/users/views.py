from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Userregestration

# Create your views here.

def index(request):
    # return HttpResponse("Index_ecom1")
    return render(request,'users/index.html')

def login(request):
    return render(request,'users/login.html')

def singup(request):
    return render(request,'users/singup.html')

def singup2(request):
    if request.method == 'POST':
        form = Userregestration(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('success')
            return redirect('login')
    else:
        form = Userregestration()
    return render(request, 'users/singup2.html', {'form': form})
