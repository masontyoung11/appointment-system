from django.db import models

# Create your models here.
class Appointments(models.Model):
    type = models.CharField(max_length=100)
    energy_usage = models.FloatField()
    time_choice = models.CharField(max_length=100)
    date = models.DateField()
