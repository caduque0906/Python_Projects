# Generated by Django 2.1.5 on 2023-07-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20230702_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('treats', 'treats'), ('drinks', 'drinks'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
