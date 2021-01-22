from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
# Create your views here.

"""
def home(request):
    return render(request, 'home.html', {})
"""


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username_login", None)
        password = request.POST.get("password_login", None)
        print(username, password)
        if True:
            user = auth.authenticate(
                request, username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'ok success')
                return redirect('home')
            messages.error(request, "Username or password may be incorrect")

            return render(request, 'login.html', {"username": username, "password": password})
            # {"data": "username or password may be incorrect "})
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username_register', None)
        password = request.POST.get('password_register', None)
        email = request.POST.get('email_register', None)
        try:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            auth.login(request, user)
        except:
            messages.error(request, "Username already exists!")
            return render(request, 'register.html', {"username": username, "email": email})
        return redirect('home')

    return render(request, 'register.html', {})


def logout(request):
    auth.logout(request)
    return redirect("login")
