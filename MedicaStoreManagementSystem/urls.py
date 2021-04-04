
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from MedicalStoreApp import views
router = routers.DefaultRouter()
router.register("company/",views.CompanySerializer)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api',include(router.urls))
]
