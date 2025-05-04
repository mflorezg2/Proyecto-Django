from django.db import models

class Service(models.Model):
    service_id = models.CharField(max_length=255)
    service_date = models.DateTimeField()
    summary = models.TextField()
    entry_date = models.DateField()
    exit_date = models.DateField()

    def __str__(self):
        return f"Service {self.service_id}"

