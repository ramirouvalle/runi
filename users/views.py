from django.contrib.auth import authenticate
from django.shortcuts import render

from .forms import LoginForm, RegisterForm


def login(request):
    if request.method == 'POST':
        print(request.POST)
        form = LoginForm(request.POST)

        if form.is_valid():
            print('valid')
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                print('user exists')
            else:
                print('user does not exists')
        else:
            print('invalid')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        print(request.POST)
        form = RegisterForm(request.POST)

        if form.is_valid():
            print('user created')
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {'form': form})
