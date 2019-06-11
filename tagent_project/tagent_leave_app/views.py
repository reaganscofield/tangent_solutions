from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee, Leave
from .serializers import EmployeeSerializer, LeaveSerializer


class EmployeeViews(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class LeaveViews(viewsets.ModelViewSet): 
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
