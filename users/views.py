from django.contrib.auth import authenticate
from django.shortcuts import render

from .forms import LoginForm


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
