# Generated by Django 4.2.6 on 2023-10-28 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshopapp', '0003_frame_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshopapp.frame')),
            ],
        ),
    ]
