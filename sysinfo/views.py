from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import (
    Doctor,
    Disease,
    Department,
    Hospital,
    Patient,
    Treatment,
)
from sysinfo.forms import DoctorForm, DiseaseForm, DepartmentForm, HospitalForm, PatientForm, TreatmentForm
from .utils import PageLinksMixin


class DoctorList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Doctor


class DoctorDetail(DetailView):
    model = Doctor

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        doctor = self.get_object()
        disease_list = doctor.diseases.all()
        context['disease_list'] = disease_list
        return context


class DoctorCreate(CreateView):
    form_class = DoctorForm
    model = Doctor


class DoctorUpdate(UpdateView):
    form_class = DoctorForm
    model = Doctor
    template_name = 'sysinfo/doctor_form_update.html'


class DoctorDelete(DeleteView):
    model = Doctor
    success_url = reverse_lazy('sysinfo_doctor_list_urlpattern')

    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        diseases = doctor.diseases.all()
        if diseases.count() > 0:
            return render(
                request,
                'sysinfo/doctor_refuse_delete.html',
                {'doctor': doctor,
                 'diseases': diseases,
                 }
            )
        else:
            return render(
                request,
                'sysinfo/doctor_confirm_delete.html',
                {'doctor': doctor}
            )


class DiseaseList(ListView):
    model = Disease


class DiseaseDetail(DetailView):
    model = Disease

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        disease = self.get_object()
        hospital = disease.hospital
        department = disease.department
        doctor = disease.doctor
        treatment_list = disease.treatments.all()
        context['hospital'] = hospital
        context['department'] = department
        context['doctor'] = doctor
        context['treatment_list'] = treatment_list
        return context


class DiseaseCreate(CreateView):
    form_class = DiseaseForm
    model = Disease


class DiseaseUpdate(UpdateView):
    form_class = DiseaseForm
    model = Disease
    template_name = 'sysinfo/disease_form_update.html'


class DiseaseDelete(DeleteView):
    model = Disease
    success_url = reverse_lazy('sysinfo_disease_list_urlpattern')

    def get(self, request, pk):
        disease = get_object_or_404(Disease, pk=pk)
        treatments = disease.treatments.all()
        if treatments.count() > 0:
            return render(
                request,
                'sysinfo/disease_refuse_delete.html',
                {'disease': disease,
                 'treatments': treatments,
                 }
            )
        else:
            return render(
                request,
                'sysinfo/disease_confirm_delete.html',
                {'disease': disease}
            )


class DepartmentList(ListView):
    model = Department


class DepartmentDetail(DetailView):
    model = Department

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        department = self.get_object()
        disease_list = department.diseases.all()
        context['disease_list'] = disease_list
        return context


class DepartmentCreate(CreateView):
    form_class = DepartmentForm
    model = Department


class DepartmentUpdate(UpdateView):
    form_class = DepartmentForm
    model = Department
    template_name = 'sysinfo/department_form_update.html'


class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('sysinfo_department_list_urlpattern')

    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        diseases = department.diseases.all()
        if diseases.count() > 0:
            return render(
                request,
                'sysinfo/department_refuse_delete.html',
                {'department': department,
                 'diseases': diseases,
                 }
            )
        else:
            return render(
                request,
                'sysinfo/department_confirm_delete.html',
                {'department': department}
            )


class HospitalList(ListView):
    model = Hospital


class HospitalDetail(DetailView):
    model = Hospital

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        hospital = self.get_object()
        disease_list = hospital.diseases.all()
        context['disease_list'] = disease_list
        return context


class HospitalCreate(CreateView):
    form_class = HospitalForm
    model = Hospital


class HospitalUpdate(UpdateView):
    form_class = HospitalForm
    model = Hospital
    template_name = 'sysinfo/hospital_form_update.html'


class HospitalDelete(DeleteView):
    model = Hospital
    success_url = reverse_lazy('sysinfo_hospital_list_urlpattern')

    def get(self, request, pk):
        hospital = get_object_or_404(Hospital, pk=pk)
        diseases = hospital.diseases.all()
        if diseases.count() > 0:
            return render(
                request,
                'sysinfo/hospital_refuse_delete.html',
                {'hospital': hospital,
                 'diseases': diseases,
                 }
            )
        else:
            return render(
                request,
                'sysinfo/hospital_confirm_delete.html',
                {'hospital': hospital}
            )


class PatientList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Patient
    permission_required = 'sysinfo.view_patient'


class PatientDetail(DetailView):
    model = Patient

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        patient = self.get_object()
        treatment_list = patient.treatments.all()
        context['treatment_list'] = treatment_list
        return context


class PatientCreate(CreateView):
    form_class = PatientForm
    model = Patient


class PatientUpdate(UpdateView):
    form_class = PatientForm
    model = Patient
    template_name = 'sysinfo/patient_form_update.html'


class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('sysinfo_patient_list_urlpattern')

    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        treatments = patient.treatments.all()
        if treatments.count() > 0:
            return render(
                request,
                'sysinfo/patient_refuse_delete.html',
                {'patient': patient,
                 'treatments': treatments,
                 }
            )
        else:
            return render(
                request,
                'sysinfo/patient_confirm_delete.html',
                {'patient': patient}
            )


class TreatmentList(ListView):
    model = Treatment


class TreatmentDetail(DetailView):
    model = Treatment

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        treatment = self.get_object()
        patient = treatment.patient
        disease = treatment.disease
        context['patient'] = patient
        context['disease'] = disease
        return context


class TreatmentCreate(CreateView):
    form_class = TreatmentForm
    model = Treatment


class TreatmentUpdate(UpdateView):
    form_class = TreatmentForm
    model = Treatment
    template_name = 'sysinfo/treatment_form_update.html'


class TreatmentDelete(DeleteView):
    model = Treatment
    success_url = reverse_lazy('sysinfo_treatment_list_urlpattern')
