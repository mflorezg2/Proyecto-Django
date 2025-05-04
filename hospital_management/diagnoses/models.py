from django.db import models

class Diagnosis(models.Model):
    diagnosis_id = models.CharField(max_length=255)
    diagnosis_date = models.DateField()
    summary = models.TextField()
    result = models.TextField()
    medical_board = models.TextField()

    def __str__(self):
        return f"Diagnosis {self.diagnosis_id}"

