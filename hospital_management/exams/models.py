from django.db import models

class Exam(models.Model):
    exam_name = models.CharField(max_length=255)
    exam_date = models.DateField()
    patient_id = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)  # Relación con Paciente

    def __str__(self):
        return self.exam_name

