# Generated by Django 4.2.6 on 2023-10-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshopapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='frame',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='frame',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]