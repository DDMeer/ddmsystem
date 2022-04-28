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
)

urlpatterns = [

    path('doctor/',
         DoctorList.as_view(),
         name='sysinfo_doctor_list_urlpattern'),

    path('doctor/<int:pk>/',
         DoctorDetail.as_view(),
         name='sysinfo_doctor_detail_urlpattern'),

    path('disease/',
         DiseaseList.as_view(),
         name='sysinfo_disease_list_urlpattern'),

    path('disease/<int:pk>/',
         DiseaseDetail.as_view(),
         name='sysinfo_disease_detail_urlpattern'),

    path('department/',
         DepartmentList.as_view(),
         name='sysinfo_department_list_view'),

    path('department/<int:pk>/',
         DepartmentDetail.as_view(),
         name='sysinfo_department_detail_urlpattern'),

    path('hospital/',
         HospitalList.as_view(),
         name='sysinfo_hospital_list_urlpattern'),

    path('hospital/<int:pk>/',
         HospitalDetail.as_view(),
         name='sysinfo_hospital_detail_urlpattern'),

    path('patient/',
         PatientList.as_view(),
         name='sysinfo_patient_list_urlpattern'),

    path('patient/<int:pk>/',
         PatientDetail.as_view(),
         name='sysinfo_patient_detail_urlpattern'),

    path('treatment/',
         TreatmentList.as_view(),
         name='sysinfo_treatment_list_urlpattern'),

    path('treatment/<int:pk>/',
         TreatmentDetail.as_view(),
         name='sysinfo_treatment_detail_urlpattern'),

]
