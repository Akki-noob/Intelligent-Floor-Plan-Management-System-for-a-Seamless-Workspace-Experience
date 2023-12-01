from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Floor(models.Model):
    floor_number=models.IntegerField(unique=True)

    def __str__(self):
        return str(self.floor_number)

    class Meta:
        verbose_name = ("Floor")
        verbose_name_plural = ("Floors")
        ordering = ["floor_number"]

class Cubicle(models.Model):
    cubicle_number=models.IntegerField(unique=True)
    floor_number=models.ForeignKey(Floor,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cubicle_number)

    class Meta:
        verbose_name = ("Cubicle")
        verbose_name_plural = ("Cubicles")
        ordering = ["cubicle_number"]

class Employee(models.Model):
    employee_id=models.IntegerField(unique=True)
    employee_name=models.CharField(max_length=255)

    def __str__(self):
        return str(self.employee_id)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")
        ordering = ["employee_id"]

class Seating(models.Model):
    seating_id=models.AutoField(primary_key=True)
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    cubicle_id=models.ForeignKey(Cubicle,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.seating_id)

    class Meta:
        verbose_name = ("Seating")
        verbose_name_plural = ("Seatings")
        ordering = ["seating_id"]
