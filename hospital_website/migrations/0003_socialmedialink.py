# Generated by Django 4.0.10 on 2023-08-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_website', '0002_remove_workinghours_hours_workinghours_closing_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.URLField()),
                ('whatsapp_link', models.URLField()),
                ('linkedIn_link', models.URLField()),
                ('twitter_link', models.URLField()),
            ],
        ),
    ]
