# Generated by Django 4.0.10 on 2023-09-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_services', '0003_serviceoffered_iconinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='category_name',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
