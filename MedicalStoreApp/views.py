from django.shortcuts import render
from rest_framework import viewsets
from MedicalStoreApp.serializers import CompanySerializer
from MedicalStoreApp.models import Company

class CompanyViewSet(viewsets.ModelViewSet):
    def list(self,request):
        Company = Company.objects.all()
    queryset = CompanySerializer(Company,many=True,context={"request":request})