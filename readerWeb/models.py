from django.db import models


# Create your models here.
class ReadCommend(models.Model):
    chipId = models.CharField(blank=True, max_length=20)
    token = models.CharField(blank=True, max_length=50)
    status = models.IntegerField(blank=True, default=0)
