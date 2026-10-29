from api.models import *
from rest_framework.response import Response
from api.serializers import *
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status


class StudentViewSet(viewsets.ViewSet):
    def list(self, req):
        print("*******lIST*******")
        print("Base Name:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, req, pk=None):
        print("*******Retrieve*******")
        print("Base Name:", self.basename)
        print("Action:", self.action)   
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        if pk is None:
              return Response({'error': 'Student ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
          stu = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found with this ID'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, req):
        print("*******Create*******")
        print("Base Name:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, req, pk):
        print("*******Update*******")
        print("Base Name:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        if pk is None:
            return Response({'error': 'Student ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            stu = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found with this ID'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(stu, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, req, pk):
        print("*******Partial Update*******")
        print("Base Name:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        if pk is None:
            return Response({'error': 'Student ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            stu = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found with this ID'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(stu, data=req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, req, pk=None):
        print("*******Destroy*******")
        print("Base Name:", self.basename)  
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        if pk is None:
            return Response({'error': 'Student ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            stu = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found with this ID'}, status=status.HTTP_404_NOT_FOUND)
        stu.delete()
        return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
 
