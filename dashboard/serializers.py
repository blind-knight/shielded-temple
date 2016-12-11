from rest_framework import serializers
from .models import toDoList, patient, case

class toDoListSerializer(serializers.ModelSerializer):

	class Meta:
		model = toDoList
		fields = '__all__'

class patientSerializer(serializers.ModelSerializer):

	class Meta:
		model = patient
		fields = '__all__'

class caseSerializer(serializers.ModelSerializer):
	patientob = patientSerializer()

	class Meta:
		model = case
		fields = '__all__'