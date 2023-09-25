# Generated by Django 4.0.10 on 2023-09-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_website', '0008_remove_aboutlist_related_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedialink',
            name='facebook_link',
            field=models.URLField(blank=True, default='https://www.facebook.com/', null=True),
        ),
        migrations.AlterField(
            model_name='socialmedialink',
            name='linkedIn_link',
            field=models.URLField(blank=True, default='https://www.linkedin.com/', null=True),
        ),
        migrations.AlterField(
            model_name='socialmedialink',
            name='twitter_link',
            field=models.URLField(blank=True, default='https://twitter.com', null=True),
        ),
        migrations.AlterField(
            model_name='socialmedialink',
            name='whatsapp_link',
            field=models.URLField(blank=True, default='https://web.whatsapp.com', null=True),
        ),
        migrations.AlterField(
            model_name='topfootercontent',
            name='url',
            field=models.URLField(blank=True, default='https://..', null=True),
        ),
    ]
