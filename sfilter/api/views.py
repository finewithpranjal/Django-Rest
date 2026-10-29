from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.filters import SearchFilter


# Create your views here.
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^branch'] # Search for students whose branch starts with the search character.
    # search_fields = ['branch']
    # search_fields = ['=branch'] # Search for students whose branch is exactly equal to the search character.