# Generated by Django 3.2.9 on 2021-12-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
