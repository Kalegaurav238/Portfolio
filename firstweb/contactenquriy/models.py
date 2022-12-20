from django.db import models

class contactenquriy(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    project = models.TextField()
    message = models.TextField()
# Create your models here.
