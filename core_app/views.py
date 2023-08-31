from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
# from .forms import CustomUserCreationForm
# from .models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

@login_required

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method=="POST":
        get_username=request.POST.get('username')
        get_password=request.POST.get('password')
        get_confirm_password=request.POST.get('repassword')
        if get_password!=get_confirm_password:
            messages.info(request,'Password is not matching')
            return redirect('signup')
        
        try:
            if User.objects.get(username=get_username):
                messages.warning(request,"Username is Taken")
                return redirect('signup')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(get_username,get_username,get_password)
        myuser.save()

        myuser= authenticate(username=get_username,password=get_password)

        if myuser is not None:

            login(request,myuser)
            messages.success(request,"User Created Successfully")
            return redirect('login')
   
    return render(request,'core/signup.html')

def user_login(request):
    if request.method=="POST":
        get_username=request.POST.get('username')
        get_password=request.POST.get('password')
        myuser=authenticate(username=get_username,password=get_password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('frontpage')
        else:
            messages.error(request,"Invalid Username or Password")
    
    return render(request, 'core/login.html')

@login_required

def user_logout(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect('login')
