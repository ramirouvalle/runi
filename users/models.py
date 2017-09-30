from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=10)
    cell_phone_number = models.CharField(max_length=12)
    student_number = models.CharField(max_length=7)
