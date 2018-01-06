from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as fun_login, logout as fun_logout

from .forms import LoginForm, RegisterForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            fun_login(request, User.objects.get(username=form.cleaned_data.get('username')))
            return redirect('rides:rides')
    else:
        if request.user.is_active:
            return redirect('rides:rides')
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    saved_message = "Usuario registrado correctamente."

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/register.html", {'saved_message': saved_message})
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {'form': form, 'saved_message': saved_message})


@login_required(login_url='users:login')
def logout(request):
    fun_logout(request)
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
