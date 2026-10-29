from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes



@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(req, pk=None):
    if req.method == 'GET':
     id = pk
     if id is not None:
        try:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found with this id'}, status=404)
    
     stu = Student.objects.all()
     serializer = StudentSerializer(stu, many=True)
     return Response(serializer.data)

    if req.method == 'POST':
       serializer = StudentSerializer(data=req.data)
       if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Data Created'}, status=201)
       return Response(serializer.errors, status=400)

    if req.method == 'PUT':
        id = pk
        if id is None:
            return Response({'error': 'ID is required for update'}, status=400)
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found with this id'}, status=404)
        
        serializer = StudentSerializer(stu, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated Completly'}, status=200)
        return Response(serializer.errors, status=400)

    if req.method == 'PATCH':
        id = pk
        if id is None:
            return Response({'error': 'ID is required for update'}, status=400)
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found with this id'}, status=404)
        
        serializer = StudentSerializer(stu, data=req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'}, status=200)
        return Response(serializer.errors, status=400)

    if req.method == 'DELETE':
       id = pk
       if id is None:
          return Response({'error': 'ID is required for delete'}, status=400)
       try:
          stu = Student.objects.get(id=pk)
          stu.delete()
          return Response({'msg': 'Data Deleted'}, status = 200)
       except Student.DoesNotExist:
          return Response({'error': 'Student with this id, not found'}, status=404)


# Below ...
'''
The above code defines a Django REST Framework API view for managing Student records. for api testing we are using 'applicaton.py' file.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(req):
    if req.method == 'GET':
     id = req.data.get('id')
     if id is not None:
        try:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found with this id'}, status=404)
    
     stu = Student.objects.all()
     serializer = StudentSerializer(stu, many=True)
     return Response(serializer.data)

    if req.method == 'POST':
       serializer = StudentSerializer(data=req.data)
       if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Data Created'}, status=201)
       return Response(serializer.errors, status=400)

    if req.method == 'PUT':
        id = req.data.get('id')
        if id is None:
            return Response({'error': 'ID is required for update'}, status=400)
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found with this id'}, status=404)
        
        serializer = StudentSerializer(stu, data=req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'}, status=200)
        return Response(serializer.errors, status=400)

    if req.method == 'DELETE':
       id = req.data.get('id')
       if id is None:
          return Response({'error': 'ID is required for delete'}, status=400)
       try:
          stu = Student.objects.get(id=id)
          stu.delete()
          return Response({'msg': 'Data Deleted'}, status = 200)
       except Student.DoesNotExist:
          return Response({'error': 'Student with this id, not found'}, status=404)

          '''
       