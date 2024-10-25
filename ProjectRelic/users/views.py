from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Userregestration
from .models import Accounts
from shop.models import Products
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def login(request):
    products = Products.objects.all()
    if request.method == 'POST':
        e_mail = request.POST.get('e_mail')
        password = request.POST.get('password')
        account = get_object_or_404(Accounts,e_mail=e_mail)
        if account.password == password:
            # return HttpResponseRedirect('index',{'products':products,'account':account})
            # return redirect('index')
            return render(request,'shop/index.html',{'products':products,'account':account})
        else:
            return HttpResponse("ERROR")
    
    return render(request,'users/login.html')
        
        
def singup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        e_mail = request.POST.get('e_mail')
        phone_nub = request.POST.get('phone_number')

        form_data = Accounts(firstname=first_name,lastname=last_name,e_mail=e_mail,phone_no=phone_nub)
        # form_data.save()
        # try:
        #     form_data.save()
        # except:
        #     return 'Account alredy exiests !plese login.'
        # return redirect('login')
    else:
        print(request)
        return render(request,'users/singup.html')

def verify_email(request):
    email = request.POST.get('email')
    response_data = {
            'is_taken': Accounts.objects.filter(e_mail=email).exists()
    }
    return JsonResponse(response_data)

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
