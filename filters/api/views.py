from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.models import Student
from api.serializers import StudentSerializer

# Create your views here.
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        HOD = self.request.user
        return Student.objects.filter(passby=HOD)
