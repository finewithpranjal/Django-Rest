from api.models import *
from api.serializers import *
from rest_framework import viewsets




class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer





'''
Read only model view set : the user can only read the data but cannot modify it, it allows read only actions such as list and retrieve. It does not allow create, update, or delete actions.

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
'''