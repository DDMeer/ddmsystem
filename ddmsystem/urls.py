"""ddmsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path

from sysinfo.views import (
    doctor_list_view,
    disease_list_view,
    hospital_list_view,
    department_list_view,
    patient_list_view,
    treatment_list_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/', doctor_list_view),
    path('disease/', disease_list_view),
    path('department/', department_list_view),
    path('hospital/', hospital_list_view),
    path('patient/', patient_list_view),
    path('treatment/', treatment_list_view),
]


