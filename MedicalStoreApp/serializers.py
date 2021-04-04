from rest_framework import serializers
from MedicalStoreApp.models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name','lisence_no','adress','contact_no','email','description']

