from django.db import models

class Patient(models.Model):
    patient_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=5)
    allergies = models.TextField()
    medical_conditions = models.TextField()

    def __str__(self):
        return self.name

