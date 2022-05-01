from django import forms

from sysinfo.models import Doctor, Disease, Department, Hospital, Patient, Treatment


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = '__all__'

    def clean_disease_name(self):
        return self.cleaned_data['disease_name'].strip()


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

    def clean_department_number(self):
        return self.cleaned_data['department_number'].strip()

    def clean_department_name(self):
        return self.cleaned_data['department_name'].strip()


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'
