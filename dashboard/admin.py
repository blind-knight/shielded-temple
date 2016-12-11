from django.contrib import admin

from .models import toDoList, patient, case


admin.site.register(toDoList)
admin.site.register(patient)
admin.site.register(case)