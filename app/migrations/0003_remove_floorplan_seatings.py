# Generated by Django 4.0.4 on 2023-12-01 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_seating_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floorplan',
            name='seatings',
        ),
    ]