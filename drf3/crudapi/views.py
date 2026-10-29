from django.http import JsonResponse
from django.shortcuts import render
from crudapi.models import Student
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from crudapi.serializers import StudentSerializer
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, req, *args, **kwargs):
        json_data = req.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream) # Decrialization
        id = py_data.get('id', None)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)  # Serialization
                serialized_data = StudentSerializer(stu)
                return JsonResponse(serialized_data.data)
            except Student.DoesNotExist:
                return JsonResponse({'msg' : 'Student with this ID does not exist'}, safe=False)

        stu = Student.objects.all()
        serialized_data = StudentSerializer(stu, many=True)
        return JsonResponse(serialized_data.data, safe=False)

    def post(self, req, *args, **kwargs):
        json_data = req.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream) # Decrialization
        serialized_data = StudentSerializer(data=py_data)
        if serialized_data.is_valid():
            serialized_data.save()
            msg = {'msg': 'Data Created'}
            return JsonResponse(msg, safe=False)
        return JsonResponse(serialized_data.errors, safe=False)

    def put(self, req, *args, **kwargs):
        json_data = req.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream) # Decrialization
        id = py_data.get('id')
        stu = Student.objects.get(id=id)
        serialized_data = StudentSerializer(stu, data=py_data, partial=True) 
        if serialized_data.is_valid():
            serialized_data.save()
            msg = {'msg': 'Data Updated!!'}
            return JsonResponse(msg, safe=False)
        return JsonResponse(serialized_data.errors, safe=False)

    def delete(self, req, *args, **kwargs ):
        json_data = req.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream) # Decrialization
        id = py_data.get('id')
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                stu.delete()
                msg = {'msg' : 'Data Deleted!!'}
                return JsonResponse(msg, safe=False)
            except Student.DoesNotExist:
                return JsonResponse({'msg' : 'Student with this ID does not exist'}, safe=False)

        return JsonResponse({'msg' : 'Please provide a valid ID'}, safe=False)
  

# View for getiing data
# @csrf_exempt
# def student_api(req):
#   if req.method == 'GET':
#     json_data = req.body
#     stream = io.BytesIO(json_data)
#     py_data = JSONParser().parse(stream) # Decrialization
#     id = py_data.get('id', None)
#     if id is not None:
#       try:
#           stu = Student.objects.get(id=id)  # Serialization
#           serialized_data = StudentSerializer(stu)
#           return JsonResponse(serialized_data.data)
#       except Student.DoesNotExist:
#           return JsonResponse({'msg' : 'Student with this ID does not exist'}, safe=False)
      
#     stu = Student.objects.all()
#     serialized_data = StudentSerializer(stu, many=True)
#     return JsonResponse(serialized_data.data, safe=False)

#   if req.method == 'POST':
#     json_data = req.body
#     stream = io.BytesIO(json_data)
#     py_data = JSONParser().parse(stream) # Decrialization
#     serialized_data = StudentSerializer(data=py_data)
#     if serialized_data.is_valid():
#       serialized_data.save()
#       msg = {'msg': 'Data Created'}
#       return JsonResponse(msg, safe=False)
#     return JsonResponse(serialized_data.errors, safe=False)

#   if req.method == 'PUT':
#     json_data = req.body
#     stream = io.BytesIO(json_data)
#     py_data = JSONParser().parse(stream) # Decrialization
#     id = py_data.get('id')
#     stu = Student.objects.get(id=id)
#     serialized_data = StudentSerializer(stu, data=py_data, partial=True) 
#     if serialized_data.is_valid():
#       serialized_data.save()
#       msg = {'msg': 'Data Updated!!'}
#       return JsonResponse(msg, safe=False)
#     return JsonResponse(serialized_data.errors, safe=False)

#   if req.method == 'DELETE':
#     json_data = req.body
#     stream = io.BytesIO(json_data)
#     py_data = JSONParser().parse(stream) # Decrialization
#     id = py_data.get('id')
#     if id is not None:
#      try:
#          stu = Student.objects.get(id=id)
#          stu.delete()
#          msg = {'msg' : 'Data Deleted!!'}
#          return JsonResponse(msg, safe=False)
#      except Student.DoesNotExist:
#          return JsonResponse({'msg' : 'Student with this ID does not exist'}, safe=False)
     
#     return JsonResponse({'msg' : 'Please provide a valid ID'}, safe=False)
  






  
