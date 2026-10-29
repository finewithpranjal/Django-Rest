from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.models import Student
from api.serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['passby', 'branch']
