# Generated by Django 3.2.13 on 2022-04-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['department_number', 'department_name']},
        ),
        migrations.AddConstraint(
            model_name='department',
            constraint=models.UniqueConstraint(fields=('department_number', 'department_name'), name='unique_department'),
        ),
    ]