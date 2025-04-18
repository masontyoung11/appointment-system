from django.db import models

# Create your models here.
class carbonFootprint(models.Model):
    carbon_footprint = models.FloatField()
    
    # Add a foreign key to the user model
    # user = models.ForeignKey(User, on_delete=models.CASCADE)