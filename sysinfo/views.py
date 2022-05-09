from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class DoctorList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Doctor
    permission_required = 'sysinfo.view_doctor'


class DoctorDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Doctor
    permission_required = 'sysinfo.view_doctor'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        doctor = self.get_object()
        disease_list = doctor.diseases.all()
        context['disease_list'] = disease_list
        return context


class DoctorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = DoctorForm
    model = Doctor
    permission_required = 'sysinfo.add_doctor'


class DoctorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = DoctorForm
    model = Doctor
    template_name = 'sysinfo/doctor_form_update.html'
    permission_required = 'sysinfo.change_doctor'


class DoctorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy('sysinfo_doctor_list_urlpattern')
    permission_required = 'sysinfo.delete_doctor'

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


class DiseaseList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Disease
    permission_required = 'sysinfo.view_disease'


class DiseaseDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Disease
    permission_required = 'sysinfo.view_disease'

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


class DiseaseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = DiseaseForm
    model = Disease
    permission_required = 'sysinfo.add_disease'


class DiseaseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = DiseaseForm
    model = Disease
    template_name = 'sysinfo/disease_form_update.html'
    permission_required = 'sysinfo.change_disease'


class DiseaseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Disease
    success_url = reverse_lazy('sysinfo_disease_list_urlpattern')
    permission_required = 'sysinfo.delete_disease'

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


class DepartmentList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Department
    permission_required = 'sysinfo.view_department'


class DepartmentDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Department
    permission_required = 'sysinfo.view_department'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        department = self.get_object()
        disease_list = department.diseases.all()
        context['disease_list'] = disease_list
        return context


class DepartmentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = DepartmentForm
    model = Department
    permission_required = 'sysinfo.add_department'


class DepartmentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = DepartmentForm
    model = Department
    template_name = 'sysinfo/department_form_update.html'
    permission_required = 'sysinfo.change_department'


class DepartmentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Department
    success_url = reverse_lazy('sysinfo_department_list_urlpattern')
    permission_required = 'sysinfo.delete_department'

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


class HospitalList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Hospital
    permission_required = 'sysinfo.view_hospital'


class HospitalDetail(DetailView):
    model = Hospital
    permission_required = 'sysinfo.view_hospital'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        hospital = self.get_object()
        disease_list = hospital.diseases.all()
        context['disease_list'] = disease_list
        return context


class HospitalCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = HospitalForm
    model = Hospital
    permission_required = 'sysinfo.add_hospital'


class HospitalUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = HospitalForm
    model = Hospital
    template_name = 'sysinfo/hospital_form_update.html'
    permission_required = 'sysinfo.change_hospital'


class HospitalDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Hospital
    success_url = reverse_lazy('sysinfo_hospital_list_urlpattern')
    permission_required = 'sysinfo.delete_hospital'

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


class PatientList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Patient
    permission_required = 'sysinfo.view_patient'


class PatientDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Patient
    permission_required = 'sysinfo.view_patient'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        patient = self.get_object()
        treatment_list = patient.treatments.all()
        context['treatment_list'] = treatment_list
        return context


class PatientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PatientForm
    model = Patient
    permission_required = 'sysinfo.add_patient'


class PatientUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PatientForm
    model = Patient
    template_name = 'sysinfo/patient_form_update.html'
    permission_required = 'sysinfo.change_patient'


class PatientDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('sysinfo_patient_list_urlpattern')
    permission_required = 'sysinfo.delete_patient'

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


class TreatmentList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Treatment
    permission_required = 'sysinfo.view_treatment'


class TreatmentDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Treatment
    permission_required = 'sysinfo.view_treatment'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        treatment = self.get_object()
        patient = treatment.patient
        disease = treatment.disease
        context['patient'] = patient
        context['disease'] = disease
        return context


class TreatmentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TreatmentForm
    model = Treatment
    permission_required = 'sysinfo.add_treatment'


class TreatmentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = TreatmentForm
    model = Treatment
    template_name = 'sysinfo/treatment_form_update.html'
    permission_required = 'sysinfo.change_treatment'


class TreatmentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Treatment
    success_url = reverse_lazy('sysinfo_treatment_list_urlpattern')
    permission_required = 'sysinfo.delete_treatment'

