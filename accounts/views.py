from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in now !')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Username/Password !')
            return redirect('login')
    return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'The username already exists !')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'The email id is alraedy registered !')
                else:
                    user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
                    user.save()
                    auth.login(request,user)
                    messages.success(request,f'Welcome {firstname}, Happy Shopping!')
                    return redirect ('dashboard')

        else:
            messages.error(request,'The password entered did not match')
            return redirect('register')
    return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are successfully logged out !')
        return redirect('home')
    return redirect('home')