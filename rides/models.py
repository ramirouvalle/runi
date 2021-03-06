from decimal import Decimal
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Day(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Ride(models.Model):
    title = models.CharField(max_length=80, null=False)
    location = models.CharField(max_length=100, null=False)
    destination = models.ForeignKey(Destination)
    days = models.ManyToManyField(Day)
    hour = models.TimeField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    passengers = models.PositiveIntegerField()
    price = models.DecimalField(default=0, decimal_places=2, max_digits=12,
                                validators=[MinValueValidator(Decimal('0.01'))])
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'location': self.location,
            'destination': self.destination,
            'hour': self.hour,
            'description': self.description,
            'user': self.user.username
        }


class RideRequest(models.Model):
    user = models.ForeignKey(User)
    ride = models.ForeignKey(Ride)
    created_at = models.DateTimeField(auto_now_add=True)
