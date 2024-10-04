from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Userregestration
from .models import Accounts
from django.shortcuts import get_object_or_404


# Create your views here.

def login(request):
    if request.method == 'Post':
        e_mail = request.POST.get('E_mail')
        password = request.POST.get('passowrd')
        confirm_password = request.POST.get('confirm_password')
        account = get_object_or_404(Accounts,e_mail=e_mail)
        if password == confirm_password:
            if password == account.password:
                return render(request,'shop/index.html',{'account':account})
            else:
                return redirect('404')
        else:
            return redirect("worng passowrd")
        
        
def singup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        e_mail = request.POST.get('e_mail')
        phone_nub = request.POST.get('phone_number')

        print(first_name,last_name,e_mail,phone_nub)

        form_data = Accounts(firstname=first_name,lastname=last_name,e_mail=e_mail,phone_no=phone_nub).save()
        # form_data.save()
        return redirect('login')
    
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
