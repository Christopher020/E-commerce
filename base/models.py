from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.FileField(upload_to='product/', null=True)  
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    miles = models.IntegerField()
    location = models.CharField(max_length=5000, blank=False)
    used_or_new = models.CharField(max_length=10, blank=False)
    price = models.IntegerField()
    engine_type = models.CharField(max_length=5000, blank=False)
    Transmission = models.CharField(max_length=20, blank=False)
    fuel_type = models.CharField(max_length=6, blank=False)
    interior_color = models.CharField(max_length=20, blank=False)
    Exterior_color = models.CharField(max_length=20, blank=False)
    vehicle_id = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
