from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import (
    Doctor,
    Disease,
    Department,
    Hospital,
    Patient,
    Treatment,
)
from sysinfo.forms import DoctorForm, DiseaseForm, DepartmentForm, HospitalForm, PatientForm, TreatmentForm
from .utils import ObjectCreateMixin


# class DoctorList(View):
#
#     def get(self, request):
#         return render(
#             request,
#             'sysinfo/doctor_list.html',
#             {'doctor_list': Doctor.objects.all()}
#         )
class DoctorList(View):
    page_kwarg = 'page'
    paginate_by = 25;  # 25 doctors per page
    template_name = 'sysinfo/doctor_list.html'

    def get(self, request):
        doctors = Doctor.objects.all()
        paginator = Paginator(
            doctors,
            self.paginate_by
        )
        page_number = request.GET.get(
            self.page_kwarg
        )
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'doctor_list': page,
        }
        return render(
            request, self.template_name, context)


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


class DoctorCreate(ObjectCreateMixin, View):
    form_class = DoctorForm
    template_name = 'sysinfo/doctor_form.html'


class DoctorUpdate(View):
    form_class = DoctorForm
    model = Doctor
    template_name = 'sysinfo/doctor_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        doctor = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=doctor),
            'doctor': doctor,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        doctor = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=doctor)
        if bound_form.is_valid():
            new_doctor = bound_form.save()
            return redirect(new_doctor)
        else:
            context = {
                'form': bound_form,
                'doctor': doctor,
            }
            return render(
                request,
                self.template_name,
                context)


class DoctorDelete(View):

    def get(self, request, pk):
        doctor = self.get_object(pk)
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

    def get_object(self, pk):
        return get_object_or_404(
            Doctor,
            pk=pk)

    def post(self, request, pk):
        doctor = self.get_object(pk)
        doctor.delete()
        return redirect('sysinfo_doctor_list_urlpattern')


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


class DiseaseCreate(ObjectCreateMixin, View):
    form_class = DiseaseForm
    template_name = 'sysinfo/disease_form.html'


class DiseaseUpdate(View):
    form_class = DiseaseForm
    model = Disease
    template_name = 'sysinfo/disease_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        section = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=section),
            'section': section,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        disease = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=disease)
        if bound_form.is_valid():
            new_section = bound_form.save()
            return redirect(new_section)
        else:
            context = {
                'form': bound_form,
                'disease': disease,
            }
            return render(
                request,
                self.template_name,
                context)

class DiseaseDelete(View):

    def get(self, request, pk):
        disease = self.get_object(pk)
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

    def get_object(self, pk):
        return get_object_or_404(
            Disease,
            pk=pk)

    def post(self, request, pk):
        disease = self.get_object(pk)
        disease.delete()
        return redirect('sysinfo_disease_list_urlpattern')


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


class DepartmentCreate(ObjectCreateMixin, View):
    form_class = DepartmentForm
    template_name = 'sysinfo/department_form.html'


class DepartmentUpdate(View):
    form_class = DepartmentForm
    model = Department
    template_name = 'sysinfo/department_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        department = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=department),
            'department': department,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        department = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=department)
        if bound_form.is_valid():
            new_department = bound_form.save()
            return redirect(new_department)
        else:
            context = {
                'form': bound_form,
                'department': department,
            }
            return render(
                request,
                self.template_name,
                context)


class DepartmentDelete(View):

    def get(self, request, pk):
        department = self.get_object(pk)
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

    def get_object(self, pk):
        department = get_object_or_404(
            Department,
            pk=pk
        )
        return department

    def post(self, request, pk):
        department = self.get_object(pk)
        department.delete()
        return redirect('sysinfo_department_list_urlpattern')



class HospitalList(View):

    def get(self, request):
        return render(
            request,
            'sysinfo/hospital_list.html',
            {'hospital_list': Hospital.objects.all()}
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
            {'hospital': hospital, 'disease_list': disease_list}
        )


class HospitalCreate(ObjectCreateMixin, View):
    form_class = HospitalForm
    template_name = 'sysinfo/hospital_form.html'


class HospitalUpdate(View):
    form_class = HospitalForm
    model = Hospital
    template_name = 'sysinfo/hospital_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        hospital = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=hospital),
            'hospital': hospital,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        hospital = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=hospital)
        if bound_form.is_valid():
            new_hospital = bound_form.save()
            return redirect(new_hospital)
        else:
            context = {
                'form': bound_form,
                'hospital': hospital,
            }
            return render(
                request,
                self.template_name,
                context)


class HospitalDelete(View):

    def get(self, request, pk):
        hospital = self.get_object(pk)
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

    def get_object(self, pk):
        hospital = get_object_or_404(
            Hospital,
            pk=pk
        )
        return hospital

    def post(self, request, pk):
        hospital = self.get_object(pk)
        hospital.delete()
        return redirect('sysinfo_hospital_list_urlpattern')



# class PatientList(View):
#
#     def get(self, request):
#         return render(
#             request,
#             'sysinfo/patient_list.html',
#             {'patient_list': Patient.objects.all()}
#         )
class PatientList(View):
    page_kwarg = 'page'
    paginate_by = 25;  # 25 patients per page
    template_name = 'sysinfo/patient_list.html'

    def get(self, request):
        patients = Patient.objects.all()
        paginator = Paginator(
            patients,
            self.paginate_by
        )
        page_number = request.GET.get(
            self.page_kwarg
        )
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'patient_list': page,
        }
        return render(
            request, self.template_name, context)




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


class PatientCreate(ObjectCreateMixin, View):
    form_class = PatientForm
    template_name = 'sysinfo/patient_form.html'


class PatientUpdate(View):
    form_class = PatientForm
    model = Patient
    template_name = 'sysinfo/patient_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        patient = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=patient),
            'patient': patient,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        patient = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=patient)
        if bound_form.is_valid():
            new_patient = bound_form.save()
            return redirect(new_patient)
        else:
            context = {
                'form': bound_form,
                'patient': patient,
            }
            return render(
                request,
                self.template_name,
                context)


class PatientDelete(View):

    def get(self, request, pk):
        patient = self.get_object(pk)
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

    def get_object(self, pk):
        patient = get_object_or_404(
            Patient,
            pk=pk
        )
        return patient

    def post(self, request, pk):
        patient = self.get_object(pk)
        patient.delete()
        return redirect('sysinfo_patient_list_urlpattern')


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


class TreatmentCreate(ObjectCreateMixin, View):
    form_class = TreatmentForm
    template_name = 'sysinfo/treatment_form.html'


class TreatmentUpdate(View):
    form_class = TreatmentForm
    model = Treatment
    template_name = 'sysinfo/treatment_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        treatment = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=treatment),
            'treatment': treatment,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        treatment = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=treatment)
        if bound_form.is_valid():
            new_treatment = bound_form.save()
            return redirect(new_treatment)
        else:
            context = {
                'form': bound_form,
                'treatment': treatment,
            }
            return render(
                request,
                self.template_name,
                context)


class TreatmentDelete(View):

    def get(self, request, pk):
        treatment = self.get_object(pk)
        return render(
            request,
            'sysinfo/treatment_confirm_delete.html',
            {'treatment': treatment}
        )

    def get_object(self, pk):
        treatment = get_object_or_404(
            Treatment,
            pk=pk
        )
        return treatment

    def post(self, request, pk):
        treatment = self.get_object(pk)
        treatment.delete()
        return redirect('sysinfo_treatment_list_urlpattern')
