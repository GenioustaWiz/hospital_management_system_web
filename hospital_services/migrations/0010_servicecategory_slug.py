# Generated by Django 4.0.10 on 2023-09-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_services', '0009_remove_serviceoffered_delete_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecategory',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]