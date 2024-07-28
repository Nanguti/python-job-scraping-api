import sys
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .utils import search_jobs_for_all_companies

class ScrapeJobsView(APIView):
    def get(self, request, *args, **kwargs):
        search_jobs_for_all_companies()
        return Response({'status': 'success', 'message': 'Jobs scraped and saved to database'}, status=status.HTTP_200_OK)

class JobListView(APIView):
    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()
        job_list = [{
            'company': job.company.name,
            'job_title': job.job_title,
            'link': job.link
        } for job in jobs]
        return Response({'jobs': job_list}, status=status.HTTP_200_OK)
