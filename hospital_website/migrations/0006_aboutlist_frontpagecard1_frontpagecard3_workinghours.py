
# Generated by Django 4.0.10 on 2023-07-31 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_website', '0005_alter_homepage_body_alter_topfootercontent_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='default', max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='hospital_abt_images')),
            ],
        ),
        migrations.CreateModel(
            name='FrontPageCard1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='Emergency Case', max_length=100)),
                ('body', models.CharField(default='default', max_length=200)),
                ('color', models.CharField(default='green', max_length=100)),
                ('iconInput', models.CharField(default='default', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FrontPageCard3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='Clinic Timetable', max_length=100)),
                ('body', models.CharField(default='default', max_length=200)),
                ('color', models.CharField(default='green', max_length=100)),
                ('iconInput', models.CharField(default='default', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('hours', models.CharField(max_length=100)),
            ],
        ),
    ]