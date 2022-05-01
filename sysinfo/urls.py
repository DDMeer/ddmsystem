from django.urls import path

from sysinfo.views import (
    DoctorList,
    DiseaseList,
    DepartmentList,
    HospitalList,
    PatientList,
    TreatmentList,
    DoctorDetail,
    DiseaseDetail,
    DepartmentDetail,
    HospitalDetail,
    PatientDetail,
    TreatmentDetail,
    DoctorCreate,
    DiseaseCreate,
    DepartmentCreate,
    HospitalCreate,
    PatientCreate,
    TreatmentCreate,
    DoctorUpdate,
    DiseaseUpdate,
    DepartmentUpdate,
    HospitalUpdate,
    PatientUpdate,
    TreatmentUpdate,
    DoctorDelete,
    DiseaseDelete,
    DepartmentDelete,
    HospitalDelete,
    PatientDelete,
    TreatmentDelete,
)

urlpatterns = [

    path('doctor/',
         DoctorList.as_view(),
         name='sysinfo_doctor_list_urlpattern'),

    path('doctor/<int:pk>/',
         DoctorDetail.as_view(),
         name='sysinfo_doctor_detail_urlpattern'),

    path('doctor/create/',
         DoctorCreate.as_view(),
         name='sysinfo_doctor_create_urlpattern'),

    path('doctor/<int:pk>/update/',
         DoctorUpdate.as_view(),
         name='sysinfo_doctor_update_urlpattern'),

    path('doctor/<int:pk>/delete/',
         DoctorDelete.as_view(),
         name='sysinfo_doctor_delete_urlpattern'),

    path('disease/',
         DiseaseList.as_view(),
         name='sysinfo_disease_list_urlpattern'),

    path('disease/<int:pk>/',
         DiseaseDetail.as_view(),
         name='sysinfo_disease_detail_urlpattern'),

    path('disease/Create/',
         DiseaseCreate.as_view(),
         name='sysinfo_disease_create_urlpattern'),

    path('disease/<int:pk>/update/',
         DiseaseUpdate.as_view(),
         name='sysinfo_disease_update_urlpattern'),

    path('disease/<int:pk>/delete/',
         DiseaseDelete.as_view(),
         name='sysinfo_disease_delete_urlpattern'),

    path('department/',
         DepartmentList.as_view(),
         name='sysinfo_department_list_urlpattern'),

    path('department/<int:pk>/',
         DepartmentDetail.as_view(),
         name='sysinfo_department_detail_urlpattern'),

    path('department/create/',
         DepartmentCreate.as_view(),
         name='sysinfo_department_create_urlpattern'),

    path('department/<int:pk>/update/',
         DepartmentUpdate.as_view(),
         name='sysinfo_department_update_urlpattern'),

    path('department/<int:pk>/delete/',
         DepartmentDelete.as_view(),
         name='sysinfo_department_delete_urlpattern'),

    path('hospital/',
         HospitalList.as_view(),
         name='sysinfo_hospital_list_urlpattern'),

    path('hospital/<int:pk>/',
         HospitalDetail.as_view(),
         name='sysinfo_hospital_detail_urlpattern'),

    path('hospital/create/',
         HospitalCreate.as_view(),
         name='sysinfo_hospital_create_urlpattern'),

    path('hospital/<int:pk>/update/',
         HospitalUpdate.as_view(),
         name='sysinfo_hospital_update_urlpattern'),

    path('hospital/<int:pk>/delete/',
         HospitalDelete.as_view(),
         name='sysinfo_hospital_delete_urlpattern'),

    path('patient/',
         PatientList.as_view(),
         name='sysinfo_patient_list_urlpattern'),

    path('patient/<int:pk>/',
         PatientDetail.as_view(),
         name='sysinfo_patient_detail_urlpattern'),

    path('patient/create/',
         PatientCreate.as_view(),
         name='sysinfo_patient_create_urlpattern'),

    path('patient/<int:pk>/update/',
         PatientUpdate.as_view(),
         name='sysinfo_patient_update_urlpattern'),

    path('patient/<int:pk>/delete/',
         PatientDelete.as_view(),
         name='sysinfo_patient_delete_urlpattern'),

    path('treatment/',
         TreatmentList.as_view(),
         name='sysinfo_treatment_list_urlpattern'),

    path('treatment/<int:pk>/',
         TreatmentDetail.as_view(),
         name='sysinfo_treatment_detail_urlpattern'),

    path('treatment/create/',
         TreatmentCreate.as_view(),
         name='sysinfo_treatment_create_urlpattern'),

    path('treatment/<int:pk>/update/',
         TreatmentUpdate.as_view(),
         name='sysinfo_treatment_update_urlpattern'),

    path('treatment/<int:pk>/delete/',
         TreatmentDelete.as_view(),
         name='sysinfo_treatment_delete_urlpattern'),

]
