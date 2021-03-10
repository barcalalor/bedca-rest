from django.db import models

# Masters
from authentification.models import User

class Camera(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    enable = models.BooleanField(default=True)
    lens = models.IntegerField(null=True, blank=True)
    azimuth = models.FloatField(null=True, blank=True)
    elevation = models.FloatField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    blade_length_x = models.IntegerField(default=0)
    blade_length_y = models.IntegerField(default=0)
    ground_elevation = models.IntegerField(default=0)
