from django.db import models
from django.db.models import UniqueConstraint


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_sequence = models.IntegerField(unique=True)#这个意思是在period里，summer在spring后
    city_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.city_name

    class Meta:
        ordering = ['city_sequence']


class Street(models.Model):
    street_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.street

    class Meta:
        ordering = ['street']


class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    street = models.ForeignKey(Street, related_name='hospitals', on_delete=models.PROTECT)
    city = models.ForeignKey(City, related_name='hospitals', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.street.street, self.city.city_name)

    class Meta:
        ordering = ['street__street', 'city__city_sequence']
        constraints = [
            UniqueConstraint(fields=['street', 'city'], name='unique_hospital')
        ]


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_number = models.CharField(max_length=20)
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.department_number, self.department_name)

    class Meta:
        ordering = ['department_number', 'department_name']
        constraints = [
            UniqueConstraint(fields=['department_number', 'department_name'], name='unique_department')
        ]




class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'],
                             name='unique_doctor')
        ]


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'],
                             name='unique_patient')
        ]


class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=20)
    hospital = models.ForeignKey(Hospital, related_name='diseases', on_delete=models.PROTECT)
    department = models.ForeignKey(Department, related_name='diseases', on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor, related_name='diseases', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s (%s)' % (self.department.department_number, self.disease_name, self.hospital.__str__())

    class Meta:
        ordering = ['department', 'disease_name', 'hospital']
        constraints = [
            UniqueConstraint(fields=['hospital', 'department', 'disease_name'],
                             name='unique_disease')
        ]


class Treatment(models.Model):
    treatment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, related_name='treatment', on_delete=models.PROTECT)
    disease = models.ForeignKey(Disease, related_name='treatment', on_delete=models.PROTECT)

    def __str__(self):
        return '%s / %s' % (self.disease, self.patient)

    class Meta:
        ordering = ['disease', 'patient']
        constraints = [
            UniqueConstraint(fields=['disease', 'patient'],
                             name='unique_treatment')
        ]
