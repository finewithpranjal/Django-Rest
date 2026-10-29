from django.shortcuts import render
from api.serilaizers import StudentSerializer
from api.models import Student
from rest_framework.generics import ListAPIView
from api.pagination import * # per view pagination
# Create your views here.

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #per view pagination
    pagination_class = StudentCursorPagination


