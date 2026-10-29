from django.shortcuts import render
from api.serializers import *
from api.models import *
from rest_framework import viewsets
# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
