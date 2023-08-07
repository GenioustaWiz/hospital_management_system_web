
# Generated by Django 4.0.10 on 2023-07-31 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_website', '0003_alter_aboutpage_body_alter_homepage_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=models.TextField(default='At Our Caring Hospital, we are dedicated to providing exceptional medical care with compassion and expertise. Your health and well-being are our top priorities, and we take pride in offering a wide range of medical services to meet all your healthcare needs.', max_length=600, null=True),
        ),
    ]
