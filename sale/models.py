from django.contrib.postgres.fields import ArrayField
from django.db import models
from user.models import *

# Create your models here.

class Sale(models.Model):
	name = models.CharField(max_length=128)

class Calendar(models.Model):
	sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
	date = models.DateField('Calender date')
	time = ArrayField(models.IntegerField(default=0), blank=True)
	time_zone = models.TextField(null=True)

class Meeting(models.Model):
	calender = models.ForeignKey(Calendar)
	call_request = models.ForeignKey(CallRequest)
	call_request_value = models.IntegerField()
	calender_value = models.IntegerField()


