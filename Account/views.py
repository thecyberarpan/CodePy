from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def SignUp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confpassword = request.POST.get('confpassword')
        if password != confpassword:
            return HttpResponse("your password are not matched")
        else:
            created_user = User.objects.create_user(username, email, password)
            created_user.save()
            return redirect('Login')
    return render(request, 'Account/signup.html')


@csrf_exempt
def Login(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request, username=username, password=password)
        print(username, password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('Index')
        else:
            return HttpResponse("Username or Password incorrect")
    return render(request, 'Account/login.html')



def Logout(request):
    logout(request)
    return redirect('Index')
