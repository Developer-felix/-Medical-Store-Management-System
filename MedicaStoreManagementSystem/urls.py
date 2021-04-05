
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from MedicalStoreApp.views import CompanyViewSet

router = routers.DefaultRouter()
router.register('company', CompanyViewSet,basename="company")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
