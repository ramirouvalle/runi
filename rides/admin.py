from django.contrib import admin
from .models import Ride, Day, Destination


class RideAdmin(admin.ModelAdmin):
    list_display = ('title', 'origin_direction', 'destination', 'hour', 'user', 'date_publication')


class DayAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Ride, RideAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Destination)
