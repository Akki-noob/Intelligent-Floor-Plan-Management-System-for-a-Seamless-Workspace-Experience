# Generated by Django 4.0.4 on 2023-12-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_seating_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seating',
            name='id',
        ),
        migrations.AlterField(
            model_name='seating',
            name='seating_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
