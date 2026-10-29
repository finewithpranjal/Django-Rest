from django.shortcuts import render
from api.serializers import *
from api.models import *
from rest_framework import viewsets
# Create your views here.

class SingerViewSet(viewsets.ModelViewSet):
   queryset = Singer.objects.all()
   serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
   queryset = Song.objects.all()
   serializer_class = SongSerializer

