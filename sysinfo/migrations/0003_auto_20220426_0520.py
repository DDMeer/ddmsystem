# Generated by Django 3.2.13 on 2022-04-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysinfo', '0002_auto_20220426_0437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['city_sequence']},
        ),
        migrations.AlterModelOptions(
            name='disease',
            options={'ordering': ['department', 'disease_name', 'hospital']},
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['last_name', 'first_name', 'disambiguator']},
        ),
        migrations.AlterModelOptions(
            name='hospital',
            options={'ordering': ['street__street', 'city__city_sequence']},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['last_name', 'first_name', 'disambiguator']},
        ),
        migrations.AlterModelOptions(
            name='street',
            options={'ordering': ['street']},
        ),
        migrations.AlterModelOptions(
            name='treatment',
            options={'ordering': ['disease', 'patient']},
        ),
        migrations.AlterField(
            model_name='disease',
            name='disease_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AddConstraint(
            model_name='disease',
            constraint=models.UniqueConstraint(fields=('hospital', 'department', 'disease_name'), name='unique_disease'),
        ),
        migrations.AddConstraint(
            model_name='doctor',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name', 'disambiguator'), name='unique_doctor'),
        ),
        migrations.AddConstraint(
            model_name='hospital',
            constraint=models.UniqueConstraint(fields=('street', 'city'), name='unique_hospital'),
        ),
        migrations.AddConstraint(
            model_name='patient',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name', 'disambiguator'), name='unique_patient'),
        ),
        migrations.AddConstraint(
            model_name='treatment',
            constraint=models.UniqueConstraint(fields=('disease', 'patient'), name='unique_treatment'),
        ),
    ]
