from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username:
            return render(request,'register.html',{'error':'User name is required'})

        if password1!=password2:
            return render(request,'register.html',{'error':'Passwords do not match'})

        user = User.objects.filter(username=username).exists()

        if user:
            return render(request,'register.html',{'error':'User already exists'})

        User.objects.create_user(username=username,password=password1)

        return redirect('login')
        
    return render(request,'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username:
            return render(request,'login.html',{'error':'User name is required'})
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
         
        return render(request,'login.html',{'error':'Incorrect crediantials'})
    return render(request,'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')

