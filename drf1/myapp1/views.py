from django.shortcuts import render
from myapp1.models import Student
from myapp1.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Model object - Single student data

def student_detail(req, pk):
  stu = Student.objects.get(id=pk)
#   print(stu)
  serializer = StudentSerializer(stu) # Convert model object to python data type
#   print(serializer)
#   print(serializer.data)
#   jsot_data = JSONRenderer().render(serializer.data) # Convert python data type to JSON data
#   print(jsot_data)
#   return HttpResponse(jsot_data, content_type='application/json')
  return JsonResponse(serializer.data, safe=False)
# Queryset = ALL student data
def students_detail(req):
  stu = Student.objects.all()
#   print(stu)
  serializer = StudentSerializer(stu, many=True) # Convert model object to python data type
#   print(serializer)
#   print(serializer.data)
  jsot_data = JSONRenderer().render(serializer.data) # Convert python data type to JSON data
#   print(jsot_data)
  return HttpResponse(jsot_data, content_type='application/json')