from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.filters import OrderingFilter


# Create your views here.
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name'] # Allow ordering by branch.
    # ordering_fields = ['name', 'branch'] # Allow ordering by name and branch.
    # ordering_fields = '__all__' # Allow ordering by all fields.
  