from django.db import connections
from django.db import models


class Family(models.Model):
	name = models.CharField(max_length=80, unique=True)


# Create your models here.
class Animals(models.Model):
	name = models.CharField(max_length=80)
	legs = models.IntegerField()
	weight = models.FloatField()
	height = models.FloatField()
	speed = models.IntegerField()
	family = models.ForeignKey(Family, on_delete=models.CASCADE)

