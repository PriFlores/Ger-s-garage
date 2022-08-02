from django.db import models

class Vehicles(models.Model):
    registration = models.TextField
    type = models.TextField
    makeOfCar = models.TextField
    model = models.TextField
    vehicleEngineType = models.TextField
