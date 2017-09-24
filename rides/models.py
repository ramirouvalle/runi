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
    coordinate_x = models.FloatField(null=False)
    coordinate_y = models.FloatField(null=False)

    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ride(models.Model):
    title = models.CharField(max_length=80, null=False)
    origin_direction = models.CharField(max_length=100, null=False)
    origin_coordinate_x = models.FloatField(null=False)
    origin_coordinate_y = models.FloatField(null=False)
    destination = models.ForeignKey(Destination)
    days = models.ManyToManyField(Day)
    hour = models.TimeField(null=False, blank=False)
    description = models.CharField(max_length=150, null=True, blank=True)
    user = models.ForeignKey(User)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'direction': self.origin_direction,
            'coordenates': {
                'x': self.origin_coordinate_x,
                'y': self.origin_coordinate_y
            },
            'destination': self.destination,
            'hour': self.hour,
            'description': self.description,
            'user': self.user.username
        }