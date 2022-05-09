from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    doctor_permissions = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                             content_type__model='doctor')

    patient_permissions = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                          content_type__model='patient')

    city_permissions = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                                  content_type__model='city')

    street_permissions = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                                  content_type__model='street')

    hospital_permissions = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                           content_type__model='hospital')

    department_permissions = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                         content_type__model='department')

    disease_permissions = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                          content_type__model='disease')

    treatment_permissions = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                               content_type__model='treatment')

    perm_view_doctor = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                           content_type__model='doctor',
                                                           codename='view_doctor')

    perm_view_patient = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                        content_type__model='patient',
                                                        codename='view_patient')

    perm_view_city = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                               content_type__model='city',
                                                               codename='view_city')

    perm_view_street = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                               content_type__model='street',
                                                               codename='view_street')

    perm_view_hospital = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                         content_type__model='hospital',
                                                         codename='view_hospital')

    perm_view_department = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                       content_type__model='department',
                                                       codename='view_department')

    perm_view_disease = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                        content_type__model='disease',
                                                        codename='view_disease')

    perm_view_treatment = permission_class.objects.filter(content_type__app_label='sysinfo',
                                                             content_type__model='treatment',
                                                             codename='view_treatment')

    ci_user_permissions = chain(perm_view_doctor,
                                perm_view_city,
                                perm_view_street,
                                perm_view_patient,
                                perm_view_hospital,
                                perm_view_department,
                                perm_view_disease,
                                perm_view_treatment)

    ci_scheduler_permissions = chain(doctor_permissions,
                                     city_permissions,
                                     street_permissions,
                                     hospital_permissions,
                                     department_permissions,
                                     disease_permissions,
                                     perm_view_patient,
                                     perm_view_treatment)

    ci_registrar_permissions = chain(patient_permissions,
                                     treatment_permissions,
                                     perm_view_doctor,
                                     perm_view_city,
                                     perm_view_street,
                                     perm_view_department,
                                     perm_view_hospital,
                                     perm_view_disease)

    my_groups_initialization_list = [
        {
            "name": "ci_user",
            "permissions_list": ci_user_permissions,
        },
        {
            "name": "ci_scheduler",
            "permissions_list": ci_scheduler_permissions,
        },
        {
            "name": "ci_registrar",
            "permissions_list": ci_registrar_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('sysinfo', '0006_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
