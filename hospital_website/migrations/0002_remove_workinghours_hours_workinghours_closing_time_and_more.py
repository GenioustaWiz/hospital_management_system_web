# Generated by Django 4.0.10 on 2023-08-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workinghours',
            name='hours',
        ),
        migrations.AddField(
            model_name='workinghours',
            name='closing_time',
            field=models.TimeField(default='18:00'),
        ),
        migrations.AddField(
            model_name='workinghours',
            name='opening_time',
            field=models.TimeField(default='08:00'),
        ),
        migrations.AlterField(
            model_name='workinghours',
            name='day',
            field=models.CharField(max_length=20),
        ),
    ]
