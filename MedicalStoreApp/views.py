from django.shortcuts import render
from rest_framework import viewsets
from MedicalStoreApp.serializers import CompanySerializer
from MedicalStoreApp.models import Company
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    def list(self,request):
        Company = Company.objects.all()
        serializer = CompanySerializer(Company,many=True,context={"request":request})
        response_dict = {"error":False,"Message":"All company list Data","data":serializer.data}
        return Response(response_dict)

company_list = CompanyViewSet.as_view({"get":"list"})