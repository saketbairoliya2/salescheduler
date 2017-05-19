from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=128)

class CallRequest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField('request date')
	time = ArrayField(models.IntegerField(default=0), blank=True)
	time_zone = models.TextField(null=True)

