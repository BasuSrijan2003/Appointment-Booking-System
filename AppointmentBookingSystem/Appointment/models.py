from django.db import models

# Create your models here.

class Appointments(models.Model):
    Name = models.CharField(max_length=100, default = '')
    Email = models.CharField(max_length=100, default = '', primary_key=True)
    Guests = models.IntegerField()
    Children = models.IntegerField()
    Date = models.DateField()
    Time = models.CharField(max_length = 30)

