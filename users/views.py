from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('rides:rides')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/register.html", {'saved': True})
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {'form': form})
