from django.shortcuts import render
from .models import (
    Doctor,
    Disease,
    Department,
    Hospital,
    Patient,
    Treatment,
)


def doctor_list_view(request):
    doctor_list = Doctor.objects.all()
    # doctor_list = Doctor.objects.none()
    return render(request, 'sysinfo/doctor_list.html', {'doctor_list': doctor_list})


def disease_list_view(request):
    disease_list = Disease.objects.all()
    # disease_list = Disease.objects.none()
    return render(request, 'sysinfo/disease_list.html', {'disease_list': disease_list})


def department_list_view(request):
    department_list = Department.objects.all()
    # department_list = Department.objects.none()
    return render(request, 'sysinfo/department_list.html', {'department_list': department_list})


def hospital_list_view(request):
    hospital_list = Hospital.objects.all()
    # hospital_list = Hospital.objects.none()
    return render(request, 'sysinfo/hospital_list.html', {'hospital_list': hospital_list})


def patient_list_view(request):
    patient_list = Patient.objects.all()
    # patient_list = Patient.objects.none()
    return render(request, 'sysinfo/patient_list.html', {'patient_list': patient_list})


def treatment_list_view(request):
    treatment_list = Treatment.objects.all()
    # treatment_list = Treatment.objects.none()
    return render(request, 'sysinfo/treatment_list.html', {'treatment_list': treatment_list})
