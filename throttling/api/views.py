from api.models import *
from api.serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from api.throttling import StudentRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Limiting the number of requests per user and anonymous users using throttling classes
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    throttle_classes = [StudentRateThrottle, AnonRateThrottle]