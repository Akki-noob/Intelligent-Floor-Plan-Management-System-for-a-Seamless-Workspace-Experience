# Generated by Django 4.0.4 on 2023-12-01 13:08

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cubicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cubicle_number', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Cubicle',
                'verbose_name_plural': 'Cubicles',
                'ordering': ['cubicle_number'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(unique=True)),
                ('employee_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'ordering': ['employee_id'],
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_number', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Floor',
                'verbose_name_plural': 'Floors',
                'ordering': ['floor_number'],
            },
        ),
        migrations.CreateModel(
            name='FloorPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floorPlan_id', models.IntegerField(auto_created=True, unique=True)),
                ('seatings', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seating_id', models.IntegerField(auto_created=True, unique=True)),
                ('cubicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cubicle')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
                ('floorPlan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.floorplan')),
            ],
            options={
                'verbose_name': 'Seating',
                'verbose_name_plural': 'Seatings',
                'ordering': ['employee_id', 'cubicle_id', 'seating_id'],
            },
        ),
        migrations.AddField(
            model_name='cubicle',
            name='floor_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.floor'),
        ),
    ]