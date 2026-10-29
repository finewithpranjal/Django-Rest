from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import status

class StudentAPI(APIView):
   def get(self, req, pk=None, format=None):
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
      

   def post(self, req, format=None):
       serializer = StudentSerializer(data=req.data)
       if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Data Created'}, status=201)
       return Response(serializer.errors, status=400)


   def put(self, req, pk, format=None):
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
   

   def patch(self, req, pk=None, format=None):
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
            return Response({'msg': 'Data Updated Partially'}, status=200)
        return Response(serializer.errors, status=400)
   

   def delete(self, req, pk=None, format=None):
       id = pk
       if id is None:
          return Response({'error': 'ID is required for delete'}, status=400)
       try:
          stu = Student.objects.get(id=pk)
          stu.delete()
          return Response({'msg': 'Data Deleted'}, status = 200)
       except Student.DoesNotExist:
          return Response({'error': 'Student with this id, not found'}, status=404)



       