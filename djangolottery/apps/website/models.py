from django.db import models

class Participants(models.Model):
	name = models.CharField(max_length=64)
	email = models.CharField(max_length=128)
	bcaddress = models.CharField(max_length=34)
	amount = models.FloatField(max_length=30)