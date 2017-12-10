from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=64, widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data
        pw1 = data.get('password')
        pw2 = data.get('confirm_password')

        if User.objects.filter(username=data.get('username')).exists():
            raise ValidationError('Nombre de usuario existente.')

        if pw1 != pw2:
            raise ValidationError("La contraseña no coincide, verifique nuevamente.")

    def save(self):
        data = self.cleaned_data
        user = User(username=data.get('username'), email=data.get('email'))
        user.set_password(data.get('password'))
        user.save()
        print('User: ' + user.username + ' was saved')
