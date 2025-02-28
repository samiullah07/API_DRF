from django.shortcuts import render
from rest_framework import viewsets
from .models import Companies
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=["get"])
    def employees(self,request,pk=None):
        try:
            company = Companies.objects.get(pk=pk)
            employees = Employees.objects.filter(company=company)
            emps_serilizers = EmployeesSerializer(employees,many=True,context={"request":request})

            return Response(emps_serilizers.data)
        except Exception as e:
            print(e)
            return Response({
                "message" : "Company Does not exit"
            })

        



class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
