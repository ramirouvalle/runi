from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as fun_login, logout as fun_logout
from django.views import View

from rides.models import Ride
from .forms import LoginForm, RegisterForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            fun_login(request, User.objects.get(username=form.cleaned_data.get('username')))
            return redirect('rides:rides')
        else:
            messages.error(request, form.non_field_errors())
    else:
        if request.user.is_active:
            return redirect('rides:rides')
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha registrado correctamente')
            return redirect('users:login')
        else:
            messages.error(request, form.non_field_errors())
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {'form': form})


@login_required(login_url='users:login')
def logout(request):
    fun_logout(request)
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


class UserRidesView(View):
    def get(self, request, username):
        user_owner = get_object_or_404(User, username=username)
        rides = Ride.objects.filter(user=user_owner)

        return render(request, 'rides/ride_list.html',
                      {'user_owner': user_owner, 'rides': [ride.as_dict for ride in rides]})
