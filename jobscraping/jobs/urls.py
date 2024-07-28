from django.urls import path
from .views import ScrapeJobsView, JobListView

urlpatterns = [
    path('scrape-jobs/', ScrapeJobsView.as_view(), name='scrape-jobs'),
    path('jobs/', JobListView.as_view(), name='job-list'),
]