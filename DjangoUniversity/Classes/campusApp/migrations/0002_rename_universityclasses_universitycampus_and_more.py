# Generated by Django 4.2.3 on 2023-07-06 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UniversityClasses',
            new_name='UniversityCampus',
        ),
        migrations.AlterModelOptions(
            name='universitycampus',
            options={'verbose_name_plural': 'University Campus'},
        ),
    ]
