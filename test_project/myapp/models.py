from django.db import models

# Create your models here.

class Datas(models.Model):
    name = models.CharField(max_length=20)
    contactnumber = models.CharField(max_length=10)
