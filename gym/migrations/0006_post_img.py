# Generated by Django 3.2.9 on 2021-12-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
