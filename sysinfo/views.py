from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import (
    Doctor,
    Disease,
    Department,
    Hospital,
    Patient,
    Treatment,
)


class DoctorList(View):

    def get(self, request):
        return render(
            request,
            'sysinfo/doctor_list.html',
            {'doctor_list': Doctor.objects.all()}
        )


class DoctorDetail(View):

    def get(self, request, pk):
        doctor = get_object_or_404(
            Doctor,
            pk=pk
        )
        disease_list = doctor.diseases.all()
        return render(
            request,
            'sysinfo/doctor_detail.html',
            {'doctor': doctor, 'disease_list': disease_list}
        )


class DiseaseList(View):

    def get(self, request):
        return render(
            request,
            'sysinfo/disease_list.html',
            {'disease_list': Disease.objects.all()}
        )


class DiseaseDetail(View):

    def get(self, request, pk):
        disease = get_object_or_404(
            Disease,
            pk=pk
        )
        hospital = disease.hospital
        department = disease.department
        doctor = disease.doctor
        treatment_list = disease.treatments.all()
        return render(
            request,
            'sysinfo/disease_detail.html',
            {'disease': disease,
             'hospital': hospital,
             'department': department,
             'doctor': doctor,
             'treatment_list': treatment_list}
        )


class DepartmentList(View):

    def get(self, request):
        return render(
            request,
            'sysinfo/department_list.html',
            {'department_list': Department.objects.all()}
        )


class DepartmentDetail(View):

    def get(self, request, pk):
        department = get_object_or_404(
            Department,
            pk=pk
        )
        disease_list = department.diseases.all()
        return render(
            request,
            'sysinfo/department_detail.html',
            {'department': department, 'disease_list': disease_list}
        )


class HospitalList(View):

    def get(self, request):
        return render(
            request,
            'sysinfo/hospital_list.html',
            {'semester_list': Hospital.objects.all()}
        )


class HospitalDetail(View):

    def get(self, request, pk):
        hospital = get_object_or_404(
            Hospital,
            pk=pk
        )
        disease_list = hospital.diseases.all()
        return render(
            request,
            'sysinfo/hospital_detail.html',
            {'hospital': hospital, 'section_list': disease_list}
        )


class PatientList(View):

    def get(self, request):
        return render(
            request,
            'sysinfo/patient_list.html',
            {'patient_list': Patient.objects.all()}
        )


class PatientDetail(View):

    def get(self, request, pk):
        patient = get_object_or_404(
            Patient,
            pk=pk
        )
        treatment_list = patient.treatments.all()
        return render(
            request,
            'sysinfo/patient_detail.html',
            {'patient': patient, 'treatment_list': treatment_list}
        )


class TreatmentList(View):

    def get(self, request):
        return render(
            request,
            'sysinfo/treatment_list.html',
            {'treatment_list': Treatment.objects.all()}
        )


class TreatmentDetail(View):

    def get(self, request, pk):
        treatment = get_object_or_404(
            Treatment,
            pk=pk
        )
        return render(
            request,
            'sysinfo/treatment_detail.html',
            {'treatment': treatment, 'patient': treatment.patient, 'disease': treatment.disease}
        )
