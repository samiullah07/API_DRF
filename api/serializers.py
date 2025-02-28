from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
    model = Companies
    fields = "__all__"


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Employees
    fields = "__all__"