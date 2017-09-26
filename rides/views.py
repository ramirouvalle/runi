from django.shortcuts import render
from django.views.generic import ListView, DetailView

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

class RideDetailView(DetailView):
    model = Ride
    template_name = 'rides/ride_detail.html'
    context_object_name = 'ride'

    def get_context_data(self, **kwargs):
        context = super(RideDetailView, self).get_context_data(**kwargs)
        return context