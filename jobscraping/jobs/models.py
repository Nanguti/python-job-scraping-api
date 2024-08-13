from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
