from django import forms

from .models import Ride


class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = '__all__'
