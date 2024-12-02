from django.db import models
from .consts import *

# Create your models here.
class Eventos(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.CharField(null=False, max_length=1000)
    created_date = models.DateField(auto_now_add=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    local = models.CharField(blank=True, max_length=100)
    price = models.IntegerField(blank=True)
    logo = models.ImageField(blank=True, null=True, upload_to='media/')
