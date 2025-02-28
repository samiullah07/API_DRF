from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
