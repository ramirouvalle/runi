from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import RideForm
from .models import Ride


def home(request):
    return render(request, 'rides/base.html')


@method_decorator(login_required(login_url='users:login'), 'dispatch')
class RidesListView(ListView):
    model = Ride
    context_object_name = 'rides'
    template_name = 'rides/ride_list.html'
    ordering = ['-date_publication']

    def get_queryset(self):
        return Ride.objects.all()


@method_decorator(login_required(login_url='users:login'), 'dispatch')
class RideDetailView(DetailView):
    model = Ride
    template_name = 'rides/ride_detail.html'
    context_object_name = 'ride'

    def get_context_data(self, **kwargs):
        context = super(RideDetailView, self).get_context_data(**kwargs)
        return context


class NewRideView(View):
    def get(self, request):
        form = RideForm()
        return render(request, 'rides/new_ride.html', {'form': form})
