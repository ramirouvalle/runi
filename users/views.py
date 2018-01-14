from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as fun_login, logout as fun_logout
from django.views import View

from rides.models import Ride
from users.models import Profile
from .forms import LoginForm, RegisterForm, UserProfileForm


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
            messages.success(request, 'Usuario registrado correctamente')
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
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        rides = Ride.objects.filter(user=user)

        return render(request, 'users/user_ride_list.html', {'user_profile': profile, 'rides': rides})


class UserProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        rides = Ride.objects.filter(user=user)[:3]
        return render(request, 'users/user_profile.html', {'user_profile': profile, 'rides': rides})


class UserEditProfileView(LoginRequiredMixin, View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)

        if request.user == user:
            profile = get_object_or_404(Profile, user=user)
            form = UserProfileForm(instance=profile)
            return render(request, 'users/user_edit_profile.html', {'form': form})
        else:
            return redirect('users:user_profile', username=username)

    def post(self, request, username):
        user = get_object_or_404(User, username=username)

        if request.user == user:
            profile = get_object_or_404(Profile, user=user)
            form = UserProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Perfil actualizado correctamente")
                return redirect('users:user_profile', username=username)

        else:
            return redirect('users:user_profile', username=username)
