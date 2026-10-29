from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['url', 'id', 'name', 'roll', 'city']