from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Usuário Incorreto')
            return redirect('core:login')
    else:
        return render(request,'login.html')
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')