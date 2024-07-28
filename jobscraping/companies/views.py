from rest_framework import generics
from .models import Company
from .serializers import CompanySerializers

class CompanyListView(CompanySerializers):
    query_set = Company.objects.all()
    serializer_class = CompanySerializers