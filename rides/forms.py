from django import forms

from .models import Ride


class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        exclude = ('user', 'rating')
