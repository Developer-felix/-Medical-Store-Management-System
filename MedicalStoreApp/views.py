from django.shortcuts import render
from rest_framework import viewsets
from MedicalStoreApp.serializers import CompanySerializer
from MedicalStoreApp.models import Company

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer