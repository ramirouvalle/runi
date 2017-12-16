from django.contrib.auth.models import User
from django.db import models

DAYS = (
    ('1', 'Lunes'),
    ('2', 'Martes'),
    ('3', 'Miercoles'),
    ('4', 'Jueves'),
    ('5', 'Viernes'),
    ('6', 'Sábado'),
    ('7', 'Domingo'),
)

DESTINATIONS = (
    ('universidad', 'Ciudad Universitaria'),
    ('mederos', 'Campus Mederos'),
    ('hospital', 'Campus Hospital'),
)


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
    rating = models.FloatField(default=0)
    passengers = models.PositiveIntegerField()
    price = models.FloatField(default=0)
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
