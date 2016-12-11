from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class toDoList(models.Model):
	toDoPost = models.CharField(max_length = 300)
	author = models.ForeignKey('auth.User')
	created_date = models.DateTimeField(
            default=timezone.now)

	def __str__(self):
		return self.toDoPost

class patient(models.Model):
	patientId = models.CharField(max_length = 10)
	doc = models.ForeignKey('auth.User')
	created_date = models.DateTimeField(
            default=timezone.now)

	def __str__(self):
		return self.patientId

class case(models.Model):
	patientob = models.ForeignKey(patient, on_delete=models.CASCADE, null=True)
	created_date = models.DateTimeField(
            default=timezone.now)
	Age = models.CharField('Age:', max_length=20)
	Gender = models.BooleanField('Gender:',default=1)
	Pulse = models.CharField(max_length = 20)
	BloodP = models.CharField(max_length = 20)
	RespirationR = models.CharField(max_length = 20)
	Height = models.CharField(max_length = 20)
	HeightUnits = models.CharField(max_length=20, default='cm')
	Weight = models.CharField(max_length = 20)
	WeightUnits = models.CharField(max_length=20, default='kg')
	BMI = models.CharField(max_length = 20)
	Pallor = models.BooleanField('Pallor:',default=0)
	Icterus = models.BooleanField('Icterus:',default=0)
	Cyanosis = models.BooleanField('Cyanosis:',default=0)
	Clubbing = models.BooleanField('Clubbing:',default=0)
	Lymphadenopathy = models.BooleanField('Lymphadenopathy:',default=0)
	ThyroidE = models.BooleanField('Thyroid Enlargement:',default=0)
	PeripheralP = models.BooleanField('Peripheral Pulse:',default=0)
	Csign = models.BooleanField('C sign:',default=0)
	Tsign = models.BooleanField('T sign:',default=0)
	Petechiae = models.BooleanField('Petechiae:',default=0)
	Purpura = models.BooleanField('Purpura:',default=0)
	Acanthosis = models.BooleanField('Acanthosis:',default=0)
	SkinTags = models.BooleanField('Skin Tags:',default=0)

	def __str__(self):
		name = str(self.pk)+'case'
		return name
