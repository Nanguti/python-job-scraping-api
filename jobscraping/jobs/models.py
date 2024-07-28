from django.db import models
from companies.models import Company


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.job_title
