from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('company','job_title', 'link')
    list_filter = ('company', 'job_title')
    search_fields = ('company', 'job_title')