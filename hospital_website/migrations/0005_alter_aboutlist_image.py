# Generated by Django 4.0.10 on 2023-09-06 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_website', '0004_homepagecard1_homepagecard3_delete_frontpagecard1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutlist',
            name='image',
            field=models.ImageField(upload_to='hospital_abt_images'),
        ),
    ]
