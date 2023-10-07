# Generated by Django 4.0.10 on 2023-10-06 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_staff', models.BooleanField(default=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('title', models.CharField(default='This is the default, title change it in profile.', max_length=200, null=True)),
                ('desc', models.TextField(default='Hey, there is a default text description about you that you can change it by clicking "Edit" or going', max_length=200, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('github', models.URLField(blank=True, default='https://www.github.com/', max_length=1000, null=True)),
                ('facebook', models.URLField(blank=True, default='https://www.facebook.com/', max_length=1000, null=True)),
                ('googleplus', models.URLField(blank=True, default='https://www.google+.com/', max_length=1000, null=True)),
                ('instagram', models.URLField(blank=True, default='https://www.instagram.com/', max_length=1000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
