from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from .forms import LoginForm
from .forms import RegistrationForm

def get_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate against Django's User model
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng')
    else:
        form = LoginForm()

    return render(request, 'LoginPage.html', {'form': form})

def get_logout(request):
    logout(request)
    return redirect('/auth/login')

def get_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])  # Set the hashed password
            user.save()
            messages.success(request, 'Đăng ký thành công! Bạn có thể đăng nhập.')
            return redirect('/auth/login')
    else:
        form = RegistrationForm()

    return render(request, 'RegisterPage.html', {'form': form})