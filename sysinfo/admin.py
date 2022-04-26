from django.contrib import admin

from .models import Hospital, Disease, Department, Doctor, Patient, Treatment, City, Street
admin.site.register(Hospital)
admin.site.register(Disease)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Treatment)
admin.site.register(City)
admin.site.register(Street)
