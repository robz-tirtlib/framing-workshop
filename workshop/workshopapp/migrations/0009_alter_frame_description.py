# Generated by Django 4.2.6 on 2023-11-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshopapp', '0008_frame_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='description',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
    ]