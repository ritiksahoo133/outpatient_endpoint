from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    max_patient = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    patient_name = models.CharField(max_length=100)

    def __str__(self):
        return self.patient_name
