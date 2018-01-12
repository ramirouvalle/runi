from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from .forms import RideForm
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


class RideDetailView(View):
    def get(self, request, pk):
        ride = get_object_or_404(Ride, pk=pk)
        return render(request, 'rides/ride_detail.html', {'ride': ride})

    def delete(self, request, pk):
        ride = get_object_or_404(Ride, pk=pk, user=request.user)
        ride.delete()
        messages.success(request, "Ride eliminado correctamente")
        return JsonResponse({'status': True})


class NewRideView(LoginRequiredMixin, View):
    def get(self, request):
        form = RideForm()
        return render(request, 'rides/ride_form.html', {'form': form})

    def post(self, request):
        form = RideForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ride creado correctamente")
            return redirect('rides:ride_detail', pk=form.instance.id)
        return render(request, 'rides/ride_form.html', {'form': form})


class EditRideView(LoginRequiredMixin, View):
    def get(self, request, pk):
        ride = get_object_or_404(Ride, pk=pk, user=request.user)
        form = RideForm(instance=ride)
        return render(request, 'rides/ride_form.html', {'form': form, 'id_ride': pk})

    def post(self, request, pk):
        ride = get_object_or_404(Ride, pk=pk, user=request.user)
        form = RideForm(request.POST, instance=ride)
        if form.is_valid():
            form.save()
            messages.success(request, "Ride modificado correctamente")
            return redirect('rides:ride_detail', pk=pk)
        return render(request, 'rides/ride_form.html', {'form': form, 'id_ride': pk})
