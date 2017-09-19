from django.shortcuts import render
from django.views.generic import ListView

from .models import Ride


def home(request):
    return render(request, 'rides/base.html')

class RidesListView(ListView):
    model = Ride
    context_object_name = 'rides'
    template_name = 'rides/ride_list.html'
    ordering = ['-date_publication']

    def get_queryset(self):
        return Ride.objects.all()