from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    cell_phone_number = models.CharField(max_length=12, null=True, blank=True)
    student_number = models.CharField(max_length=7, null=True, blank=True)
    image = models.ImageField(upload_to='users/avatar', null=True, blank=True)
