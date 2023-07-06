# Generated by Django 4.2.3 on 2023-07-06 18:22

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(blank=True, default='', max_length=60)),
                ('state', models.CharField(blank=True, default='', max_length=2)),
                ('campus_id', models.IntegerField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'University Classes',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]