from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    verbose_name_plural = "Companies"
    
    def __str__(self):
        return self.name